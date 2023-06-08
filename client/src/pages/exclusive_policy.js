import { Box, Container, Stack, Typography } from "@mui/material";
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";
import { useCallback, useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import exclusivePolicyAPI from "src/api/exclusive_policy";

const Page = () => {
  const [exclusivePolicies, setExclusivePolicies] = useState([]);
  const [deleteModalState, setDeleteModalState] = useState({
    isOpen: false,
    exclusivePolicy: null,
  });
  const [deleteManyModelIsOpen, setDeleteManyModalIsOpen] = useState(false);
  const [selectedRows, setSelectedRows] = useState([]);

  const getExclusivePoliciesHandler = async () => {
    try {
      const exclusivePolicy = await exclusivePolicyAPI.getEntities();
      setExclusivePolicies(exclusivePolicy);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getExclusivePoliciesHandler();
  }, []);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "name", headerName: "Name", width: 150 },
    { field: "descriptor", headerName: "Descriptor", width: 150 },
    { field: "price", headerName: "Price", width: 150 },
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
        <title>Exclusive Policies | Dekla Parking</title>
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
                <Typography variant="h4">Exclusive Policies</Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  <DataGrid
                    rows={exclusivePolicies}
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
