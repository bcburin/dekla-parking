import { Box, Container, Stack, Typography } from "@mui/material";
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";
import { useCallback, useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import ConfirmationModal from "src/components/confirmation-modal";
import CreateUserModal from "src/components/create-user-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import DeleteIcon from "@mui/icons-material/Delete";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import Head from "next/head";
import SecurityRoundedIcon from "@mui/icons-material/SecurityRounded";
import UpdateUserModal from "src/components/update-user-modal";
import userAPI from "src/api/users";

const Page = () => {
  const [users, setUsers] = useState([]);
  const [deleteModalState, setDeleteModalState] = useState({
    isOpen: false,
    user: null,
  });
  const [updateModalState, setUpdateModalState] = useState({
    isOpen: false,
    user: null,
  });
  const [deleteManyModelIsOpen, setDeleteManyModalIsOpen] = useState(false);
  const [createModalIsOpen, setCreateModalIsOpen] = useState(false);
  const [selectedRows, setSelectedRows] = useState([]);

  const getUsersHandler = async () => {
    try {
      const users = await userAPI.getEntities();
      setUsers(users);
    } catch (e) {
      console.log(e);
    }
  };

  const deleteUserHandler = useCallback(
    (userId) => async () => {
      try {
        setDeleteModalState({ isOpen: false, user: null });
        await userAPI.deleteEntity(userId);
        await getUsersHandler();
      } catch (e) {
        console.log(e);
      }
    },
    []
  );

  const updateUserHandler = useCallback((user) => async () => {
    try {
      setUpdateModalState({ isOpen: false, user: null });
      await userAPI.updateEntity(user.id, user);
    } catch (e) {
      console.log(e);
    }
  });

  const deleteManyUsersHandler = useCallback(async () => {
    try {
      setDeleteManyModalIsOpen(false);
      await userAPI.deleteManyEntities(selectedRows);
      await getUsersHandler();
    } catch (e) {
      console.log(e);
    }
  });

  const toggleAdminHandler = useCallback(
    (userId) => async () => {
      try {
        await userAPI.toggleAdmin(userId);
        await getUsersHandler();
      } catch (e) {
        console.log(e);
      }
    },
    []
  );

  useEffect(() => {
    getUsersHandler();
  }, []);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "username", headerName: "Username", width: 150 },
    { field: "email", headerName: "E-mail", width: 200 },
    { field: "firstName", headerName: "First Name", width: 150 },
    { field: "lastName", headerName: "Last Name", width: 150 },
    { field: "isAdmin", headerName: "Is admin?", width: 80, type: "boolean" },
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
      field: "actions",
      type: "actions",
      width: 100,
      getActions: (params) => [
        <GridActionsCellItem
          icon={<DeleteIcon />}
          label="Delete"
          onClick={() => setDeleteModalState({ user: params, isOpen: true })}
        />,
        <GridActionsCellItem
          icon={<SecurityRoundedIcon />}
          label="Toggle Admin"
          onClick={toggleAdminHandler(params.id)}
          showInMenu
        />,
        <GridActionsCellItem
          icon={<EditRoundedIcon />}
          label="Edit"
          onClick={() => setUpdateModalState({ user: params, isOpen: true })}
          showInMenu
        />,
      ],
    },
  ];

  return (
    <>
      <Head>
        <title>Users | Dekla Parking</title>
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
                <Typography variant="h4">Users</Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  <DataGrid
                    rows={users}
                    columns={columns}
                    components={{ Toolbar: ActionsToolbar }}
                    componentsProps={{
                      toolbar: {
                        onCreateClick: () => setCreateModalIsOpen(true),
                        onRefreshClick: getUsersHandler,
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
      </Box>

      <ConfirmationModal
        open={deleteModalState.isOpen}
        onClose={() => ({ isOpen: false, user: null })}
        onConfirm={deleteUserHandler(deleteModalState.user?.id)}
        title="Delete User"
        content="Are you sure you want to delete this user?"
      />

      <ConfirmationModal
        open={deleteManyModelIsOpen}
        onClose={() => setDeleteManyModalIsOpen(false)}
        onConfirm={deleteManyUsersHandler}
        title="Delete Users"
        content="Are you sure you want to delete these users?"
      />

      <CreateUserModal
        open={createModalIsOpen}
        onClose={() => setCreateModalIsOpen(false)}
        onConfirm={async () => {
          setCreateModalIsOpen(false);
          await getUsersHandler();
        }}
        title={"Create User"}
      />

      <UpdateUserModal
        open={updateModalState.isOpen}
        onClose={() => setUpdateModalState({ isOpen: false, user: null })}
        onConfirm={async () => {
          await updateUserHandler(updateModalState.user);
          await getUsersHandler();
        }}
        title={"Edit User Data"}
        user={updateModalState.user}
      />
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
