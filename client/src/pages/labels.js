import {
  Box,
  Button,
  Container,
  Grid,
  Stack,
  SvgIcon,
  Typography,
  useTheme,
} from "@mui/material";
import { useEffect, useState } from "react";

import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import CachedRoundedIcon from "@mui/icons-material/CachedRounded";
import CreateLabelModal from "src/components/label/create-label-modal";
import { Layout as DashboardLayout } from "src/layouts/dashboard/layout";
import Head from "next/head";
import LabelCard from "src/components/label/label-card";
import labelsAPI from "src/api/labels";

const Page = () => {
  const theme = useTheme();
  const [labels, setLabels] = useState([]);
  const [createLabelModalIsOpen, setCreateLabelModalIsOpen] = useState(false);

  const getLabelsHandler = async () => {
    try {
      const labels = await labelsAPI.getEntities();
      setLabels(labels);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getLabelsHandler();
  }, []);

  return (
    <>
      <Head>
        <title>Labels | Dekla Parking</title>
      </Head>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8,
        }}
      >
        <Container>
          <Stack
            direction="column"
            spacing={2}
            sx={{ marginBottom: "20px", height: "100%" }}
          >
            <Typography variant="h4">Labels</Typography>

            <Container
              sx={{
                bgcolor: theme.palette.primary.light,
                borderRadius: 4,
                padding: "24px",
                boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
                flexGrow: 1,
                width: "100%",
              }}
            >
              <Box
                sx={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                  marginBottom: "16px",
                }}
              >
                <Box sx={{ display: "flex", gap: "8px" }}>
                  <Button
                    startIcon={
                      <SvgIcon fontSize="small">
                        <AddCircleOutlinedIcon />
                      </SvgIcon>
                    }
                    variant="contained"
                    color="primary"
                    onClick={() => setCreateLabelModalIsOpen(true)}
                  >
                    Create
                  </Button>
                  <Button
                    startIcon={
                      <SvgIcon>
                        <CachedRoundedIcon />
                      </SvgIcon>
                    }
                    variant="contained"
                    onClick={getLabelsHandler}
                  >
                    Refresh
                  </Button>
                </Box>
              </Box>
              <Grid container spacing={2}>
                {labels
                  .slice()
                  .sort((a, b) => a.id - b.id)
                  .map((label) => (
                    <Grid item xs={12} sm={6} md={4} lg={3} key={label.id}>
                      <LabelCard
                        receivedLabel={label}
                        onUpdate={getLabelsHandler}
                      />
                    </Grid>
                  ))}
              </Grid>
            </Container>
          </Stack>
        </Container>
      </Box>
      {createLabelModalIsOpen && (
        <CreateLabelModal
          key={0}
          open={createLabelModalIsOpen}
          onClose={() => setCreateLabelModalIsOpen(false)}
          onConfirm={async () => {
            setCreateLabelModalIsOpen(false);
            await getLabelsHandler();
          }}
        />
      )}
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;
