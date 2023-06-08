import { Box, Container, Stack, Typography } from "@mui/material";
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";
import { useCallback, useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import publicPolicyAPI from "src/api/public_policy";

const Page = () => {
  const [publicPolicies, setPublicPolicy] = useState([]);
  const [selectedRows, setSelectedRows] = useState([]);

  const getPublicPolicyHandler = async () => {
    try {
      const publicPolicies = await publicPolicyAPI.getEntities();
      setPublicPolicy(publicPolicies);
    } catch (e) {
      console.log(e);
    }
  };
  useEffect(() => {
    getPublicPolicyHandler();
  }, []);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "name", headerName: "Policyname", width: 150 },
    { field: "descriptor", headerName: "descriptor", width: 200 },
    { field: "price", headerName: "price", width: 150 },
    {
      field: "createdAt",
      headerName: "Creation",
      width: 150,
      type: "date",
      valueGetter: ({ value }) => value && new Date(value),
    },
    {
      field: "updatedAt",
      headerName: "Last Update",
      width: 200,
      type: "dateTime",
      valueGetter: ({ value }) => value && new Date(value),
    },
  ];

  return (
    <>
      <Head>
        <title>Public Policies | Dekla Parking</title>
      </Head>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8,
        }}
      >
        <Container maxWidth="xl">
          <Stack spacing={3}>
            <Stack direction="row" justifyContent="space-between" spacing={4}>
              <Stack spacing={1}>
                <Typography variant="h4">Public Policies</Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  <DataGrid
                    rows={publicPolicies}
                    columns={columns}
                    components={{ Toolbar: ActionsToolbar }}
                    componentsProps={{
                      toolbar: {
                        deleteIsDisabled: selectedRows.length == 0,
                      },
                    }}
                    checkboxSelection
                    disableRowSelectionOnClick
                    onRowSelectionModelChange={(ids) => setSelectedRows(ids)}
                  />
                </Stack>
              </Stack>
            </Stack>
          </Stack>
        </Container>
      </Box>
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
