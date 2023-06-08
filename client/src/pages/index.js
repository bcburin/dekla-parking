import { Box, Unstable_Grid2 as Grid } from "@mui/material";

import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";

const Page = () => (
  <>
    <Head>
      <title>Dekla Parking</title>
    </Head>
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 8,
      }}
    ></Box>
  </>
);

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
