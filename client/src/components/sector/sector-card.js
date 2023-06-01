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

import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import DeleteRoundedIcon from "@mui/icons-material/DeleteRounded";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";
import LotCard from "./lot-card";
import React from "react";

const SectorCard = ({ sector }) => {
  const theme = useTheme();

  return (
    <Container
      sx={{
        bgcolor: theme.palette.primary.light,
        borderRadius: 4,
        padding: "24px",
        boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
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
          >
            Create
          </Button>
          <Button
            startIcon={
              <SvgIcon fontSize="small">
                <DeleteRoundedIcon />
              </SvgIcon>
            }
            variant="contained"
            color="primary"
          >
            Dismantle
          </Button>
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
          <Button
            startIcon={
              <SvgIcon fontSize="small">
                <InfoRoundedIcon />
              </SvgIcon>
            }
            variant="contained"
            color="primary"
          >
            View
          </Button>
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
  );
};

export default SectorCard;
