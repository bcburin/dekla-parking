import { Box, Container, Stack, Typography } from "@mui/material";
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";
import { useCallback, useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import ConfirmationModal from "src/components/confirmation-modal";
import CreatePermissionModal from "src/components/policy/create-permission-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import DeleteIcon from "@mui/icons-material/Delete";
import Head from "next/head";
import epPermissionAPI from "src/api/ep_permission";

const Page = () => {
  const [ep_permissions, setEpPermission] = useState([]);
  const [deleteModalState, setDeleteModalState] = useState({
    isOpen: false,
    epPermission: null,
  });
  const [deleteManyModelIsOpen, setDeleteManyModalIsOpen] = useState(false);
  const [createModalIsOPen, setCreateModalIsOpen] = useState(false);
  const [selectedRows, setSelectedRows] = useState([]);

  const getEpPermissionsHandler = async () => {
    try {
      const epPermissions = await epPermissionAPI.getEntities();
      setEpPermission(epPermissions);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getEpPermissionsHandler();
  }, []);

  const deleteEpPermissionHandler = useCallback(
    (epPermissionId) => async () => {
      try {
        setDeleteModalState({ isOpen: false, epPermission: null });
        await epPermissionAPI.deleteEntity(epPermissionId);
        await getEpPermissionsHandler();
      } catch (e) {
        console.log(e);
      }
    },
    []
  );
  const deleteManyEpPermissionHandler = useCallback(async () => {
    try {
      setDeleteManyModalIsOpen(false);
      await epPermissionAPI.deleteManyEntities(selectedRows);
      await getEpPermissionsHandler();
    } catch (e) {
      console.log(e);
    }
  });
  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    {
      field: "startTime",
      headerName: "Start Time",
      width: 150,
      valueGetter: ({ value }) => (value && new Date(value)) || "No start date",
    },
    {
      field: "endTime",
      headerName: "End Time",
      width: 150,
      valueGetter: ({ value }) => (value && new Date(value)) || "No end date",
    },
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
    {
      field: "exclusivePolicy",
      headerName: "Exclusive Policy",
      width: 90,
      valueGetter: (params) => {
        return `${params.row.epPermissionExclusivePolicy?.name || ""}`;
      },
    },
    {
      field: "label",
      headerName: "Label",
      width: 90,
      valueGetter: (params) => {
        return `${params.row.epPermissionLabel?.name || ""}`;
      },
    },
    {
      field: "actions",
      type: "actions",
      width: 100,
      getActions: (params) => [
        <GridActionsCellItem
          icon={<DeleteIcon />}
          label="Delete"
          onClick={() =>
            setDeleteModalState({ epPermission: params, isOpen: true })
          }
        />,
      ],
    },
  ];

  return (
    <>
      <Head>
        <title>Permissions | Dekla Parking</title>
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
                <Typography variant="h4">
                  Exclusive Policy Permissions
                </Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  <DataGrid
                    rows={ep_permissions}
                    columns={columns}
                    components={{ Toolbar: ActionsToolbar }}
                    componentsProps={{
                      toolbar: {
                        onCreateClick: () => setCreateModalIsOpen(true),
                        onRefreshClick: getEpPermissionsHandler,
                        onDeleteClick: () => setDeleteManyModalIsOpen(true),
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
        <ConfirmationModal
          open={deleteModalState.isOpen}
          onClose={() =>
            setDeleteModalState({ isOpen: false, epPermission: null })
          }
          onConfirm={deleteEpPermissionHandler(
            deleteModalState.epPermission?.id
          )}
          title="Delete Ep permission"
          content="Are you sure you want to delete this Ep permission?"
        />

        <ConfirmationModal
          open={deleteManyModelIsOpen}
          onClose={() => setDeleteManyModalIsOpen(false)}
          onConfirm={deleteManyEpPermissionHandler}
          title="Delete Ep permissions"
          content="Are you sure you want to delete these Ep permissions?"
        />

        <CreatePermissionModal
          open={createModalIsOPen}
          onClose={() => setCreateModalIsOpen(false)}
          onConfirm={() => {
            setCreateModalIsOpen(false);
            getEpPermissionsHandler();
          }}
        />
      </Box>
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
