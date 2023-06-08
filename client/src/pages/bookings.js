import { Box, Container, Stack, Typography } from "@mui/material";
import {
  DataGrid,
  GridActionsCellItem,
  GridRenderCellParams,
} from "@mui/x-data-grid";
import { useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import ShowUserModal from "src/components/user/show-user-modal";
import ThumbDownRoundedIcon from "@mui/icons-material/ThumbDownRounded";
import ThumbUpRoundedIcon from "@mui/icons-material/ThumbUpRounded";
import bookingsAPI from "src/api/bookings";

const Page = () => {
  const [bookings, setBookings] = useState([]);

  const getBookingsHandler = async () => {
    try {
      const bookings = await bookingsAPI.getEntities();
      setBookings(bookings);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getBookingsHandler();
  }, []);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "status", headerName: "Status", width: 150 },
    {
      field: "startTime",
      headerName: "Start Time",
      width: 200,
      type: "dateTime",
      valueGetter: ({ value }) => value && new Date(value),
    },
    {
      field: "endTime",
      headerName: "End Time",
      width: 200,
      type: "dateTime",
      valueGetter: ({ value }) => value && new Date(value),
    },
    {
      field: "createdAt",
      headerName: "Book Time",
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
      field: "userId",
      headerName: "User ID",
      width: 90,
      valueGetter: (params) => {
        return `${params.row.bookingUser.id}`;
      },
    },
    {
      field: "lotId",
      headerName: "Lot ID",
      width: 90,
      valueGetter: (params) => {
        return `${params.row.bookingLot.id}`;
      },
    },
    {
      field: "actions",
      type: "actions",
      width: 100,
      getActions: (params) => [
        <GridActionsCellItem
          icon={<ThumbUpRoundedIcon />}
          label="Approve"
          onClick={async () => {
            await bookingsAPI.approve(params.id);
            await getBookingsHandler();
          }}
          showInMenu
        />,
        <GridActionsCellItem
          icon={<ThumbDownRoundedIcon />}
          label="Reject"
          onClick={async () => {
            await bookingsAPI.reject(params.id);
            await getBookingsHandler();
          }}
          showInMenu
        />,
      ],
    },
  ];

  return (
    <>
      <Head>
        <title>Bookings | Dekla Parking</title>
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
                <Typography variant="h4">Booking Requests</Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  <DataGrid
                    rows={bookings}
                    columns={columns}
                    components={{ Toolbar: ActionsToolbar }}
                    componentsProps={{
                      toolbar: {
                        onRefreshClick: getBookingsHandler,
                      },
                    }}
                    checkboxSelection
                    disableRowSelectionOnClick
                    // onRowSelectionModelChange={(ids) => setSelectedRows(ids)}
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
