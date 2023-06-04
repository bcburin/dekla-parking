import { Box, Container, Stack, Typography } from "@mui/material";
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";
import { useCallback, useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import ConfirmationModal from "src/components/confirmation-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import DeleteIcon from "@mui/icons-material/Delete";
import Head from "next/head";
import LabelingsAPI from "src/api/labelings";

const Page = () => {
  const [labelings, setLabelings] = useState([]);
  const [deleteModalState, setDeleteModalState] = useState({
    isOpen: false,
    labeling: null,
  });
  const [deleteManyModelIsOpen, setDeleteManyModalIsOpen] = useState(false);
  const [selectedRows, setSelectedRows] = useState([]);

  const getLabelingsHandler = async () => {
    try {
      const labelings = await LabelingsAPI.getEntities();
      setLabelings(labelings);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getLabelingsHandler();
  }, []);

  const deleteLabelingHandler = useCallback(
    (labelingId) => async () => {
      try {
        setDeleteModalState({ isOpen: false, labeling: null });
        await LabelingsAPI.deleteEntity(labelingId);
        await getLabelingsHandler();
      } catch (e) {
        console.log(e);
      }
    },
    []
  );
  const deleteManyLabelingsHandler = useCallback(async () => {
    try {
      setDeleteManyModalIsOpen(false);
      await labelingAPI.deleteManyEntities(selectedRows);
      await getLabelingsHandler();
    } catch (e) {
      console.log(e);
    }
  });
  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "start_time", headerName: "Start Time", width: 150 },
    { field: "end_time", headerName: "End Time", width: 150 },
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
      field: "userId",
      headerName: "User ID",
      width: 90,
      valueGetter: (params) => {
        return `${params.row.labeledUser.id}`;
      },
    },
    {
      field: "labelId",
      headerName: "Label ID",
      width: 90,
      valueGetter: (params) => {
        return `${params.row.labelingLabel.id}`;
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
          onClick={() => setDeleteModalState({ labeling: params, isOpen: true })}
        />,
      ],
    },
  ];

  return (
    <>
      <Head>
        <title>Labeling | Dekla Parking</title>
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
                <Typography variant="h4">Labelings</Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  <DataGrid
                    rows={labelings}
                    columns={columns}
                    components={{ Toolbar: ActionsToolbar }}
                    componentsProps={{
                      toolbar: {
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
        onClose={() => setDeleteModalState({ isOpen: false, labeling: null })}
        onConfirm={deleteLabelingHandler(deleteModalState.labeling?.id)}
        title="Delete Labeling"
        content="Are you sure you want to delete this labeling?"
      />

      <ConfirmationModal
        open={deleteManyModelIsOpen}
        onClose={() => setDeleteManyModalIsOpen(false)}
        onConfirm={deleteManyLabelingsHandler}
        title="Delete Labelings"
        content="Are you sure you want to delete these labelings?"
      />
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
