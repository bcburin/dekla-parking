import { Box, Container, Stack, Typography } from "@mui/material";
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";
import { useEffect, useState } from "react";

import ActionsToolbar from "src/components/actions-toolbar";
import ArrowCircleRightRoundedIcon from "@mui/icons-material/ArrowCircleRightRounded";
import AssignPolicyModal from "src/components/policy/assign-to-sector";
import ConfirmationModal from "src/components/confirmation-modal";
import CreatePolicyModal from "src/components/policy/create-policy-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import DeleteIcon from "@mui/icons-material/Delete";
import EditRoundedIcon from "@mui/icons-material/EditRounded";
import Head from "next/head";
import InfoRoundedIcon from "@mui/icons-material/InfoRounded";
import ShowPolicyModal from "src/components/policy/show-policy-modal";
import UpdatePolicyModal from "src/components/policy/update-policy-modal";
import publicPolicyAPI from "src/api/public_policy";
import sectorAPI from "src/api/sectors";

const Page = () => {
  const [publicPolicies, setPublicPolicy] = useState([]);
  const [selectedRows, setSelectedRows] = useState([]);
  const [updateModalState, setUpdateModalState] = useState({
    isOpen: false,
    policy: null,
  });
  const [deleteModalState, setDeleteModalState] = useState({
    isOpen: false,
    policy: null,
  });
  const [showModalState, setShowModalState] = useState({
    isOpen: false,
    policy: null,
  });
  const [assignModalState, setAssignModalState] = useState({
    isOpen: false,
    policy: null,
  });
  const [deleteManyModalIsOpen, setDeleteManyModalIsOpen] = useState(false);
  const [createPolicyModalIsOpen, setCreatePolicyModalIsOpen] = useState(false);

  const getPublicPolicyHandler = async () => {
    try {
      const publicPolicies = await publicPolicyAPI.getEntities();
      setPublicPolicy(publicPolicies);
    } catch (e) {
      console.log(e);
    }
  };

  const deletePolicyHandler = (policyId) => async () => {
    try {
      setDeleteModalState({ isOpen: false, policy: null });
      await publicPolicyAPI.deleteEntity(policyId);
      getPublicPolicyHandler();
    } catch (e) {
      console.log(e);
    }
  };

  const deleteManyPoliciesHandler = async () => {
    try {
      await publicPolicyAPI.deleteManyEntities(selectedRows);
      getPublicPolicyHandler();
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getPublicPolicyHandler();
  }, []);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "name", headerName: "Name", width: 150 },
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
    {
      field: "actions",
      type: "actions",
      width: 100,
      getActions: (params) => [
        <GridActionsCellItem
          icon={<DeleteIcon />}
          label="Delete"
          onClick={() =>
            setDeleteModalState({ policy: params.row, isOpen: true })
          }
        />,
        <GridActionsCellItem
          icon={<InfoRoundedIcon />}
          label="Information"
          onClick={() => setUpdateModalState({ policy: rowData, isOpen: true })}
          showInMenu
        />,
        <GridActionsCellItem
          icon={<EditRoundedIcon />}
          label="Edit"
          onClick={() =>
            setUpdateModalState({ policy: params.row, isOpen: true })
          }
          showInMenu
        />,
        <GridActionsCellItem
          icon={<ArrowCircleRightRoundedIcon />}
          label="Assign to Sector"
          onClick={() =>
            setAssignModalState({ policy: params.row, isOpen: true })
          }
          showInMenu
        />,
      ],
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
                        onRefreshClick: getPublicPolicyHandler,
                        onCreateClick: () => setCreatePolicyModalIsOpen(true),
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
        onClose={() => setDeleteModalState({ isOpen: false, policy: null })}
        onConfirm={deletePolicyHandler(deleteModalState.policy?.id)}
        title="Delete Public Policy"
        content="Are you sure you want to delete this public policy?"
      />

      <ConfirmationModal
        open={deleteManyModalIsOpen}
        onClose={() => setDeleteManyModalIsOpen(false)}
        onConfirm={deleteManyPoliciesHandler}
        title="Delete Public Policies"
        content="Are you sure you want to delete these public policies?"
      />

      <CreatePolicyModal
        open={createPolicyModalIsOpen}
        onClose={() => setCreatePolicyModalIsOpen(false)}
        onConfirm={() => {
          setCreatePolicyModalIsOpen(false);
          getPublicPolicyHandler();
        }}
        api={publicPolicyAPI}
      />

      <UpdatePolicyModal
        open={updateModalState.isOpen}
        onClose={() => setUpdateModalState({ isOpen: false, policy: null })}
        onConfirm={() => {
          setUpdateModalState({ isOpen: false, policy: null });
          getPublicPolicyHandler();
        }}
        policyData={updateModalState.policy}
        api={publicPolicyAPI}
      />

      <ShowPolicyModal
        open={showModalState.isOpen}
        onClose={() =>
          setShowModalState({
            isOpen: false,
            policy: null,
          })
        }
        policy={showModalState.policy}
      />

      <AssignPolicyModal
        open={assignModalState.isOpen}
        onClose={() =>
          setAssignModalState({
            isOpen: false,
            policy: null,
          })
        }
        onConfirm={() =>
          setAssignModalState({
            isOpen: false,
            policy: null,
          })
        }
        policy={assignModalState.policy}
        assignFn={sectorAPI.assignPublicPolicy}
      />
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
