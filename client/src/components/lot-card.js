import {
  Box,
  Button,
  Stack,
  SvgIcon,
  Typography,
  styled,
  useTheme,
} from "@mui/material";
import { Card, CardContent, CardHeader } from "@mui/material";

import DirectionsCarFilledRoundedIcon from "@mui/icons-material/DirectionsCarFilledRounded";
import React from "react";

const LotCard = ({ lot }) => {
  const theme = useTheme();

  const getColor = () => {
    return lot.occupied ? theme.palette.error.main : theme.palette.success.main;
  };

  return (
    <Card sx={{ maxWidth: 300 }}>
      <CardContent
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexDirection: "column",
          padding: theme.spacing(3),
          backgroundColor: getColor(),
          color: theme.palette.common.white,
        }}
      >
        <Stack spacing={2} alignItems="center">
          <SvgIcon
            sx={{
              fontSize: theme.typography.pxToRem(72),
            }}
          >
            <DirectionsCarFilledRoundedIcon />
          </SvgIcon>
          <Typography variant="h5" align="center">
            {lot.name}
          </Typography>
          <Typography variant="body1" align="center">
            {lot.location}
          </Typography>
        </Stack>
      </CardContent>
    </Card>
  );
};

export default LotCard;
