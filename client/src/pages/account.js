import {
  Box,
  Container,
  Unstable_Grid2 as Grid,
  Stack,
  Typography,
} from "@mui/material";

import { AccountProfile } from "src/sections/account/account-profile";
import { AccountProfileDetails } from "src/sections/account/account-profile-details";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import UpdateUserForm from "src/components/user/update-user-form";
import { useSelector } from "react-redux";

const Page = () => {
  const loggedUser = useSelector((store) => store.auth.loggedUser);

  return (
    <>
      <Head>
        <title>Account | Dekla Parking </title>
      </Head>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8,
        }}
      >
        <Container maxWidth="lg">
          <Stack spacing={3}>
            <div>
              <Typography variant="h4">Account</Typography>
            </div>
            <div>
              <Grid container spacing={3}>
                <Grid xs={12} md={6} lg={4}>
                  <AccountProfile />
                </Grid>
                <Grid xs={12} md={6} lg={8}>
                  <UpdateUserForm user={loggedUser} />
                </Grid>
              </Grid>
            </div>
          </Stack>
        </Container>
      </Box>
    </>
  );
};
Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
