import * as Yup from "yup";

import {
  Autocomplete,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import React, { useEffect, useState } from "react";

import sectorAPI from "src/api/sectors";
import { useFormik } from "formik";

const AssignPolicyModal = ({ policy, open, onClose, onConfirm, assignFn }) => {
  const [sectors, setSectors] = useState([]);

  const getSectors = async () => {
    try {
      const sectors = await sectorAPI.getEntities();
      setSectors(sectors);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getSectors();
  }, []);

  const formik = useFormik({
    initialValues: {
      sector: null,
    },
    onSubmit: async (values, helpers) => {
      try {
        await assignFn(values.sector?.id, policy.id);
        if (onConfirm) onConfirm();
      } catch (e) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: e.response?.data?.detail || e.message });
        helpers.setSubmitting(false);
      }
    },
  });

  return (
    <Dialog open={open}>
      <DialogTitle>Assign Policy to Sector</DialogTitle>
      <DialogContent>
        <form noValidate onSubmit={formik.handleSubmit}>
          <Stack spacing={3}>
            <Autocomplete
              options={sectors}
              getOptionLabel={(sector) =>
                sector?.name + ` [${sector?.id}]` || ""
              }
              renderInput={(params) => (
                <TextField
                  {...params}
                  label="Select a Sector"
                  fullWidth
                  autoFocus
                  error={!!(formik.touched.sector && formik.errors.sector)}
                  helperText={formik.touched.sector && formik.errors.sector}
                  value={formik.values.sector}
                  onBlur={formik.handleBlur}
                  InputLabelProps={{
                    shrink: true,
                  }}
                />
              )}
              onInputChange={(event, value) => {
                const selectedSector = sectors.find(
                  (sector) => sector?.name + ` [${sector?.id}]` === value
                );
                formik.setFieldValue("sector", selectedSector);
              }}
            />
            <TextField
              error={!!(formik.touched.startTime && formik.errors.startTime)}
              fullWidth
              helperText={formik.touched.startTime && formik.errors.startTime}
              name="startTime"
              label="Start Time"
              type="datetime-local"
              margin="normal"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              value={formik.values.startTime}
              InputLabelProps={{
                shrink: true,
              }}
            />

            <TextField
              error={!!(formik.touched.endTime && formik.errors.endTime)}
              fullWidth
              helperText={formik.touched.endTime && formik.errors.endTime}
              name="endTime"
              label="End Time"
              type="datetime-local"
              margin="normal"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              value={formik.values.endTime}
              InputLabelProps={{
                shrink: true,
              }}
            />
          </Stack>
          {formik.errors.submit && (
            <Typography color="error" sx={{ mt: 3 }} variant="body2">
              {formik.errors.submit}
            </Typography>
          )}
          <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button type="submit" color="primary">
              Confirm
            </Button>
          </DialogActions>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default AssignPolicyModal;
