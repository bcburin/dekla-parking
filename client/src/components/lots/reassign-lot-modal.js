import {
  Autocomplete,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
} from "@mui/material";
import React, { useCallback, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { actions } from "src/store/lot-ui-slice";
import lotsAPI from "src/api/lots";

const ReassignLotModal = ({ sectors, onReassign }) => {
  const dispatch = useDispatch();
  const [selectedSector, setSelectedSector] = useState(null);
  const reassignModalIsOpen = useSelector(
    (state) => state.lotUI.assignLotModalIsOpen
  );
  const selectedLot = useSelector((state) => state.lotUI.selectedLot);

  const handleSectorChange = (event, value) => {
    setSelectedSector(value);
  };

  const handleClose = useCallback(() => {
    setSelectedSector(null);
    dispatch(actions.closeAssignLotModal());
  }, [dispatch]);

  const handleReassign = async () => {
    try {
      await lotsAPI.assign(selectedLot.id, selectedSector.id);
      handleClose();
      await onReassign();
    } catch (e) {
      console.log(e);
    }
  };

  return (
    selectedLot && (
      <Dialog open={reassignModalIsOpen} maxWidth="sm">
        <DialogTitle>Reassign Lot</DialogTitle>
        <DialogContent>
          <Autocomplete
            options={sectors.slice().sort()}
            getOptionLabel={(sector) => sector.name}
            value={selectedSector}
            onChange={handleSectorChange}
            renderInput={(params) => (
              <TextField
                {...params}
                label="Select a Sector"
                fullWidth
                autoFocus
              />
            )}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleReassign} disabled={!selectedSector}>
            Reassign
          </Button>
        </DialogActions>
      </Dialog>
    )
  );
};

export default ReassignLotModal;
