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

const ShowPolicyModal = ({ policy, open, onClose }) => {
  const theme = useTheme();

  return (
    policy && (
      <Dialog open={open} sx={{ minWidth: "400px" }}>
        <DialogTitle sx={{ color: theme.palette.text.primary }}>
          Policy Information
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
            {policy.id}
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
            {policy.name}
          </Typography>
          {policy.descriptor && (
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
              {policy.descriptor}
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
            {formatDate(policy.createdAt)}
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
            {formatDate(policy.updatedAt)}
          </Typography>
        </DialogContent>
        <DialogActions sx={{ padding: "16px" }}>
          <Button onClick={onClose}>Close</Button>
        </DialogActions>
      </Dialog>
    )
  );
};

export default ShowPolicyModal;
