import {
  Button,
  Checkbox,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControlLabel,
  TextField,
} from "@mui/material";
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { actions } from "src/store/lot-ui-slice";
import lotsAPI from "src/api/lots";

const UpdateLotModal = ({ onUpdate }) => {
  const dispatch = useDispatch();
  const editLotModalIsOpen = useSelector(
    (store) => store.lotUI.editLotModalIsOpen
  );
  const lot = useSelector((store) => store.lotUI.selectedLot);
  console.log(lot);
  const [name, setName] = useState(lot?.name);
  const [location, setLocation] = useState(lot?.location);
  const [description, setDescription] = useState(lot?.description);
  const [available, setAvailable] = useState(lot?.available);
  console.log(name, location, description, available);

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleLocationChange = (event) => {
    setLocation(event.target.value);
  };

  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };

  const handleAvailableChange = (event) => {
    setAvailable(event.target.checked);
  };

  const handleClose = () => {
    dispatch(actions.closeEditLotModal());
  };

  const handleSave = async () => {
    const updatedLot = {
      name,
      location,
      description,
      available,
    };
    await lotsAPI.updateEntity(lot.id, updatedLot);
    await onUpdate();
    handleClose();
  };

  return (
    lot && (
      <Dialog open={editLotModalIsOpen} onClose={handleClose}>
        <DialogTitle>Edit Lot</DialogTitle>
        <DialogContent>
          <TextField
            label="Name"
            value={name}
            onChange={handleNameChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Location"
            value={location}
            onChange={handleLocationChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Description"
            value={description}
            onChange={handleDescriptionChange}
            fullWidth
            multiline
            rows={4}
            margin="normal"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={available}
                onChange={handleAvailableChange}
                color="primary"
              />
            }
            label="Available"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSave} color="primary">
            Save
          </Button>
        </DialogActions>
      </Dialog>
    )
  );
};

export default UpdateLotModal;
