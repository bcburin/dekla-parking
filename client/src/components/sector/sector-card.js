import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  Grid,
  SvgIcon,
  Typography,
  useTheme,
} from "@mui/material";

import PolicyRoundedIcon from "@mui/icons-material/PolicyRounded";
import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import DeleteRoundedIcon from "@mui/icons-material/DeleteRounded";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";
import LotCard from "../lots/lot-card";
import React, { useState } from "react";
import CreateLotModal from "../lots/create-lot-modal";
import ShowSectorModal from "./show-sector-modal";
import sectorAPI from "src/api/sectors";
import ConfirmationModal from "../confirmation-modal";

const SectorCard = ({ sector, refreshSectors }) => {
  const theme = useTheme();

  const [createLotModalIsOpen, setCreateLotModalIsOpen] = useState(false);
  const [showSectorModalIsOpen, setShowSectorModalIsOpen] = useState(false);
  const [deleteSectorModalIsOpen, setDeleteSectorModalIsOpen] = useState(false);

  const deleteSectorHandler = async () => {
    try {
      await sectorAPI.deleteEntity(sector.id);
    } catch (e) {
      console.log(e);
    } finally {
      setDeleteSectorModalIsOpen(false);
    }
  };

  return (
    <>
      <Container
        sx={{
          bgcolor: theme.palette.primary.light,
          borderRadius: 4,
          padding: "24px",
          boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
          flexGrow: 1,
          // margin: "",
          width: "100%",
        }}
      >
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: "16px",
          }}
        >
          <Typography variant="h5" component="h2">
            {sector.name}
          </Typography>
          <Box sx={{ display: "flex", gap: "8px" }}>
            <Button
              startIcon={
                <SvgIcon fontSize="small">
                  <AddCircleOutlinedIcon />
                </SvgIcon>
              }
              variant="contained"
              color="primary"
              onClick={() => setCreateLotModalIsOpen(true)}
            >
              Create Lot
            </Button>
            {sector && (
              <Button
                startIcon={
                  <SvgIcon fontSize="small">
                    <DeleteRoundedIcon />
                  </SvgIcon>
                }
                variant="contained"
                color="primary"
                onClick={() => setDeleteSectorModalIsOpen(true)}
              >
                Dismantle
              </Button>
            )}
            {sector && (
              <Button
                startIcon={
                  <SvgIcon fontSize="small">
                    <EditRoundedIcon />
                  </SvgIcon>
                }
                variant="contained"
                color="primary"
              >
                Edit
              </Button>
            )}
            {sector && (
              <Button
                startIcon={
                  <SvgIcon fontSize="small">
                    <InfoRoundedIcon />
                  </SvgIcon>
                }
                variant="contained"
                color="primary"
                onClick={() => setShowSectorModalIsOpen(true)}
              >
                View
              </Button>
            )}
            {sector && (
              <Button
                startIcon={
                  <SvgIcon fontSize="small">
                    <PolicyRoundedIcon />
                  </SvgIcon>
                }
                variant="contained"
                color="primary"
              >
                Assign Policy
              </Button>
            )}
          </Box>
        </Box>
        <Grid container spacing={2}>
          {sector.sectorLots
            .slice()
            .sort((a, b) => a.id - b.id)
            .map((lot) => (
              <Grid item xs={12} sm={6} md={4} lg={3} key={lot.id}>
                <LotCard receivedLot={lot} />
              </Grid>
            ))}
        </Grid>
      </Container>
      <CreateLotModal
        open={createLotModalIsOpen}
        onClose={() => setCreateLotModalIsOpen(false)}
        onConfirm={async () => {
          setCreateLotModalIsOpen(false);
        }}
        onRefresh={refreshSectors}
        sector={sector}
      />
      <ShowSectorModal
        open={showSectorModalIsOpen}
        onClose={() => setShowSectorModalIsOpen(false)}
        sector={sector}
      />
      <ConfirmationModal
        open={deleteSectorModalIsOpen}
        onClose={() => setDeleteSectorModalIsOpen(false)}
        onConfirm={deleteSectorHandler}
        title="Delete Sector"
        content={`Are you sure you want to delete this sector?`}
      />
    </>
  );
};

export default SectorCard;
