import { Box, Button, Container, Stack, Typography } from "@mui/material";
import { useCallback, useEffect, useState } from "react";

import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import SectorCard from "src/components/sector-card";
import sectorAPI from "src/api/sectors";

const Page = () => {
  const [sectors, setSectors] = useState([]);

  const getSectorsHandler = async () => {
    try {
      const sectors = await sectorAPI.getEntities();
      setSectors(sectors);
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
                <Button variant="contained">Button 1</Button>
                <Button variant="contained">Button 2</Button>
                <Button variant="contained">Button 3</Button>
              </Stack>
            </Stack>
            <Stack spacing={2} alignItems="center">
              {sectors.map((sector) => (
                <SectorCard key={sector.id} sector={sector} />
              ))}
            </Stack>
          </Stack>
        </Container>
      </Box>
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
