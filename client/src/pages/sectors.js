import {
  Box,
  Button,
  Container,
  Stack,
  SvgIcon,
  Typography,
} from "@mui/material";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";

import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import BookLotModal from "src/components/lots/book-lot-modal";
import CachedRoundedIcon from "@mui/icons-material/CachedRounded";
import ConfirmationModal from "src/components/confirmation-modal";
import CreateSectorModal from "src/components/sector/create-sector-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import ReassignLotModal from "src/components/lots/reassign-lot-modal";
import SectorCard from "src/components/sector/sector-card";
import ShowLotModal from "src/components/lots/show-lot-modal";
import UnassignedLotsCard from "src/components/sector/unassigned-lots-card";
import UpdateLotModal from "src/components/lots/update-lot-modal";
import { actions } from "src/store/lot-ui-slice";
import lotsAPI from "src/api/lots";
import sectorAPI from "src/api/sectors";

const Page = () => {
  const dispatch = useDispatch();
  const [sectors, setSectors] = useState([]);
  const [createSectorModalIsOpen, setCreateSectorModalIsOpen] = useState(false);
  const lotUIState = useSelector((store) => store.lotUI);
  const loggedUserIsAdmin = useSelector(
    (store) => store.auth.loggedUser?.isAdmin || false
  );
  const [unassignedLots, setUnassignedLots] = useState([]);

  const getSectorsHandler = async () => {
    try {
      const sectors = await sectorAPI.getEntities();
      setSectors(sectors);
    } catch (e) {
      console.log(e);
    }
  };

  const getUnassignedLotsHandler = async () => {
    try {
      const lots = await lotsAPI.getUnassignedLots();
      setUnassignedLots(lots);
    } catch (e) {
      console.log(e);
    }
  };

  const updateAll = async () => {
    await getSectorsHandler();
    await getUnassignedLotsHandler();
  };

  const deleteLotHandler = async () => {
    try {
      dispatch(actions.closeDeleteLotModal());
      await lotsAPI.deleteEntity(lotUIState.selectedLot.id);
      await updateAll();
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getUnassignedLotsHandler();
  }, []);

  useEffect(() => {
    getSectorsHandler();
  }, []);

  return (
    <>
      <Head>
        <title>Parking Lots | Dekla Parking</title>
      </Head>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8,
        }}
      >
        <Container>
          <Stack
            direction="column"
            spacing={2}
            sx={{ marginBottom: "20px", height: "100%" }}
          >
            <Stack
              direction="row"
              alignItems="center"
              justifyContent="space-between"
              sx={{ width: "100%", alignItems: "baseline" }}
            >
              <Typography variant="h4">Parking Lots</Typography>
              <Stack direction="row" spacing={2}>
                <Button
                  startIcon={
                    <SvgIcon>
                      <CachedRoundedIcon />
                    </SvgIcon>
                  }
                  variant="contained"
                  onClick={updateAll}
                >
                  Refresh
                </Button>
                <Button
                  startIcon={
                    <SvgIcon>
                      <AddCircleOutlinedIcon />
                    </SvgIcon>
                  }
                  variant="contained"
                  onClick={() => setCreateSectorModalIsOpen(true)}
                >
                  Create Sector
                </Button>
              </Stack>
            </Stack>
            <Stack
              spacing={5}
              alignItems="center"
              sx={{ flexGrow: 1, width: "100%" }}
            >
              {loggedUserIsAdmin && (
                <UnassignedLotsCard
                  key={-1}
                  unassignedLots={unassignedLots}
                  onUpdate={getUnassignedLotsHandler}
                />
              )}
              {sectors.map((sector) => (
                <SectorCard
                  key={sector.id}
                  sector={sector}
                  refreshSectors={updateAll}
                />
              ))}
            </Stack>
          </Stack>
        </Container>
      </Box>
      <ShowLotModal />
      <BookLotModal />
      <ReassignLotModal sectors={sectors} onReassign={updateAll} />
      <UpdateLotModal onUpdate={updateAll} />
      <ConfirmationModal
        open={lotUIState.deleteLotModalIsOpen}
        onClose={() => dispatch(actions.closeDeleteLotModal())}
        onConfirm={() => deleteLotHandler()}
        title="Delete Parking Lot"
        content={`Are you sure you want to delete this parking lot?`}
      />
      <CreateSectorModal
        open={createSectorModalIsOpen}
        onClose={() => setCreateSectorModalIsOpen(false)}
        onConfirm={() => setCreateSectorModalIsOpen(false)}
        onRefresh={updateAll}
      />
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
