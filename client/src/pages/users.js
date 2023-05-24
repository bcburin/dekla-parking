import Head from "next/head";
import {
  Box,
  Button,
  Container,
  Stack,
  SvgIcon,
  Typography,
  Grid,
} from "@mui/material";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import { DataGrid, GridActionsCellItem, GridToolbar } from "@mui/x-data-grid";
import DeleteIcon from "@mui/icons-material/Delete";
import SecurityIcon from "@mui/icons-material/Security";
import PlusIcon from "@heroicons/react/24/solid/PlusIcon";

import axios from "axios";
import { useState, useEffect, useCallback } from "react";
import ConfirmationModal from "src/components/confirmation-modal";

const Page = () => {
  const [users, setUsers] = useState([]);
  const [deleteModalState, setDeleteModalState] = useState({
    isOpen: false,
    user: null,
  });

  const fetchUserData = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/v1/users/?skip=0&limit=100"
      );
      const users = response.data;
      setUsers(users);
    } catch (e) {
      console.log(e);
    }
  };

  const deleteUser = useCallback(
    (userId) => async () => {
      try {
        setDeleteModalState({
          isOpen: false,
          user: null,
        });
        await axios.get(`http://127.0.0.1:8000/v1/users/${userId}`);
        await fetchUserData();
      } catch (e) {
        console.log(e);
      }
    },
    []
  );

  const toggleAdmin = useCallback(
    (userId) => async () => {
      try {
        await axios.put(
          `http://127.0.0.1:8000/v1/users/${userId}/toggle-admin`
        );
        await fetchUserData();
      } catch (e) {
        console.log(e);
      }
    },
    []
  );

  useEffect(() => {
    fetchUserData();
  }, []);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "username", headerName: "Username", width: 150 },
    { field: "email", headerName: "E-mail", width: 200 },
    { field: "first_name", headerName: "First Name", width: 150 },
    { field: "last_name", headerName: "Last Name", width: 150 },
    { field: "is_admin", headerName: "Is admin?", width: 80, type: "boolean" },
    {
      field: "created_at",
      headerName: "Creation",
      width: 150,
      type: "date",
      valueGetter: ({ value }) => value && new Date(value),
    },
    {
      field: "updated_at",
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
          icon={<SecurityIcon />}
          label="Toggle Admin"
          onClick={toggleAdmin(params.id)}
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
                    slots={{ toolbar: GridToolbar }}
                    checkboxSelection
                    disableRowSelectionOnClick
                  />
                </Stack>
              </Stack>
            </Stack>
          </Stack>
        </Container>
      </Box>

      <ConfirmationModal
        open={deleteModalState.isOpen}
        onClose={() =>
          setDeleteModalState({
            isOpen: false,
            user: null,
          })
        }
        onConfirm={deleteUser(deleteModalState.user?.id)}
        title="Delete User"
        content="Are you sure you want to delete this user?"
      />
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;