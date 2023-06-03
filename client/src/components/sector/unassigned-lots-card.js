import {
  Box,
  Button,
  Container,
  Grid,
  SvgIcon,
  Typography,
  useTheme,
} from "@mui/material";

import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import LotCard from "../lots/lot-card";
import React, { useEffect, useState } from "react";
import CreateLotModal from "../lots/create-lot-modal";
import lotsAPI from "src/api/lots";

const UnassignedLotsCard = () => {
  const theme = useTheme();

  const [createLotModalIsOpen, setCreateLotModalIsOpen] = useState(false);
  const [unassignedLots, setUnassignedLots] = useState([]);

  const getUnassignedLotsHandler = async () => {
    try {
      const lots = await lotsAPI.getUnassignedLots();
      setUnassignedLots(lots);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getUnassignedLotsHandler();
  }, []);

  return (
    <>
      <Container
        sx={{
          bgcolor: theme.palette.primary.light,
          borderRadius: 4,
          padding: "24px",
          boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
          flexGrow: 1,
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
            Unassigned Lots
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
          </Box>
        </Box>
        <Grid container spacing={2}>
          {unassignedLots
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
        onRefresh={getUnassignedLotsHandler}
      />
    </>
  );
};

export default UnassignedLotsCard;
