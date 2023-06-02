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

import BookLotModal from "src/components/sector/book-lot-modal";
import CachedRoundedIcon from "@mui/icons-material/CachedRounded";
import ConfirmationModal from "src/components/confirmation-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import ReassignLotModal from "src/components/sector/reassign-lot-modal";
import SectorCard from "src/components/sector/sector-card";
import ShowLotModal from "src/components/sector/show-lot-modal";
import UpdateLotModal from "src/components/sector/update-lot-modal";
import { actions } from "src/store/lot-ui-slice";
import lotsAPI from "src/api/lots";
import sectorAPI from "src/api/sectors";
import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import CreateSectorModal from "src/components/sector/create-sector-modal";

const Page = () => {
  const dispatch = useDispatch();
  const [sectors, setSectors] = useState([]);
  const [createSectorModalIsOpen, setCreateSectorModalIsOpen] = useState(false);
  const lotUIState = useSelector((state) => state.lotUI);

  const getSectorsHandler = async () => {
    try {
      const sectors = await sectorAPI.getEntities();
      setSectors(sectors);
    } catch (e) {
      console.log(e);
    }
  };

  const deleteLotHandler = async () => {
    try {
      dispatch(actions.closeDeleteLotModal());
      await lotsAPI.deleteEntity(lotUIState.selectedLot.id);
      await getSectorsHandler();
    } catch (e) {
      console.log(e);
    }
  };

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
        <Container maxWidth="xl">
          <Stack direction="column" spacing={2} sx={{ marginBottom: "20px" }}>
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
                  onClick={getSectorsHandler}
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
            <Stack spacing={2} alignItems="center">
              {sectors.map((sector) => (
                <SectorCard
                  key={sector.id}
                  sector={sector}
                  refreshSectors={getSectorsHandler}
                />
              ))}
            </Stack>
          </Stack>
        </Container>
      </Box>
      <ShowLotModal />
      <BookLotModal />
      <ReassignLotModal sectors={sectors} onReassign={getSectorsHandler} />
      <UpdateLotModal onUpdate={getSectorsHandler} />
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
        onRefresh={getSectorsHandler}
      />
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
