import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Typography,
  useTheme,
} from "@mui/material";
import { useDispatch, useSelector } from "react-redux";

import React from "react";
import { actions } from "src/store/lot-ui-slice";

const ShowLotModal = () => {
  const theme = useTheme();
  const dispatch = useDispatch();
  const lot = useSelector((store) => store.lotUI.selectedLot);
  const showLotModalIsOpen = useSelector(
    (store) => store.lotUI.showLotModalIsOpen
  );

  const getLotStatus = (lot) =>
    !lot.available ? "Unavailable" : lot.occupied ? "Occupied" : "Available";

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
    lot && (
      <Dialog open={showLotModalIsOpen} sx={{ minWidth: "400px" }}>
        <DialogTitle sx={{ color: theme.palette.text.primary }}>
          Lot Information
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
            {lot.id}
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
            {lot.name}
          </Typography>
          {lot.description && (
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
              {lot.description}
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
            {getLotStatus(lot)}
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
            {formatDate(lot.createdAt)}
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
            {formatDate(lot.updatedAt)}
          </Typography>
        </DialogContent>
        <DialogActions sx={{ padding: "16px" }}>
          <Button onClick={() => dispatch(actions.closeShowLotModal())}>
            Close
          </Button>
        </DialogActions>
      </Dialog>
    )
  );
};

export default ShowLotModal;
