import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Typography,
  useTheme,
} from "@mui/material";

import React from "react";

const ShowSectorModal = ({ sector, open, onClose }) => {
  const theme = useTheme();

  const formatDate = (datetime) => {
    const options = {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
    };
    return new Date(datetime).toLocaleString(undefined, options);
  };

  return (
    sector && (
      <Dialog open={open} sx={{ minWidth: "400px" }}>
        <DialogTitle sx={{ color: theme.palette.text.primary }}>
          Sector Information
        </DialogTitle>
        <DialogContent>
          <Typography variant="body1" sx={{ marginBottom: "8px" }}>
            <strong
              style={{
                display: "inline-block",
                minWidth: "150px",
                color: theme.palette.text.primary,
              }}
            >
              ID:
            </strong>{" "}
            {sector.id}
          </Typography>
          <Typography variant="body1" sx={{ marginBottom: "8px" }}>
            <strong
              style={{
                display: "inline-block",
                minWidth: "150px",
                color: theme.palette.text.primary,
              }}
            >
              Name:
            </strong>{" "}
            {sector.name}
          </Typography>
          {sector.description && (
            <Typography variant="body1" sx={{ marginBottom: "8px" }}>
              <strong
                style={{
                  display: "inline-block",
                  minWidth: "150px",
                  color: theme.palette.text.primary,
                }}
              >
                Description:
              </strong>{" "}
              {sector.description}
            </Typography>
          )}
          <Typography variant="body1" sx={{ marginBottom: "8px" }}>
            <strong
              style={{
                display: "inline-block",
                minWidth: "150px",
                color: theme.palette.text.primary,
              }}
            >
              Status:
            </strong>{" "}
            {sector.available ? "Available" : "Unavailable"}
          </Typography>
          <Typography variant="body1" sx={{ marginBottom: "8px" }}>
            <strong
              style={{
                display: "inline-block",
                minWidth: "150px",
                color: theme.palette.text.primary,
              }}
            >
              Creation Time:
            </strong>{" "}
            {formatDate(sector.createdAt)}
          </Typography>
          <Typography variant="body1" sx={{ marginBottom: "8px" }}>
            <strong
              style={{
                display: "inline-block",
                minWidth: "150px",
                color: theme.palette.text.primary,
              }}
            >
              Last Update Time:
            </strong>{" "}
            {formatDate(sector.updatedAt)}
          </Typography>
        </DialogContent>
        <DialogActions sx={{ padding: "16px" }}>
          <Button onClick={onClose}>Close</Button>
        </DialogActions>
      </Dialog>
    )
  );
};

export default ShowSectorModal;
