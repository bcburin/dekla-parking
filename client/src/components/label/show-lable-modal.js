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
import formatDate from "src/utils/format-date";

const ShowLabelModal = ({ label, open, onClose }) => {
  const theme = useTheme();

  return (
    label && (
      <Dialog open={open} sx={{ minWidth: "400px" }}>
        <DialogTitle sx={{ color: theme.palette.text.primary }}>
          Label Information
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
            {label.id}
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
            {label.name}
          </Typography>
          {label.description && (
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
              {label.description}
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
              Creation Time:
            </strong>{" "}
            {formatDate(label.createdAt)}
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
            {formatDate(label.updatedAt)}
          </Typography>
        </DialogContent>
        <DialogActions sx={{ padding: "16px" }}>
          <Button onClick={onClose}>Close</Button>
        </DialogActions>
      </Dialog>
    )
  );
};

export default ShowLabelModal;
