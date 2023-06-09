import * as Yup from "yup";

import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

import React from "react";
import epPermissionAPI from "src/api/ep_permission";
import { useFormik } from "formik";

const CreatePermissionModal = ({ open, onClose, onConfirm }) => {
  const formik = useFormik({
    initialValues: {
      fkEpId: 0,
      fkLabelId: 0,
      startTime: "",
      endTime: "",
    },
    validationSchema: Yup.object({
      startTime: Yup.date(),
      endTime: Yup.date().min(
        Yup.ref("startTime"),
        "End time must be after start time"
      ),
      fkEpId: Yup.number().min(0),
      fkLabelId: Yup.number().min(0),
    }),
    onSubmit: async (values, helpers) => {
      try {
        values.startTime = values.startTime || null;
        values.endTime = values.endTime || null;
        await epPermissionAPI.createEntity(values);
      } catch {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
      }
    },
  });

  return (
    <Dialog open={open}>
      <DialogTitle>Create Permission</DialogTitle>
      <DialogContent>
        <form noValidate onSubmit={formik.handleSubmit}>
          <Stack spacing={3}>
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
            <TextField
              error={!!(formik.touched.fkEpId && formik.errors.fkEpId)}
              fullWidth
              helperText={formik.touched.fkEpId && formik.errors.fkEpId}
              label="Exclusive Policy ID"
              name="fkEpId"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              type="number"
              value={formik.values.fkEpId}
            />
            <TextField
              error={!!(formik.touched.fkLabelId && formik.errors.fkLabelId)}
              fullWidth
              helperText={formik.touched.fkLabelId && formik.errors.fkLabelId}
              label="Label ID"
              name="fkLabelId"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              type="number"
              value={formik.values.fkLabelId}
            />
          </Stack>
          {formik.errors.submit && (
            <Typography color="error" sx={{ mt: 3 }} variant="body2">
              {formik.errors.submit}
            </Typography>
          )}
          <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button type="submit" color="primary" onClick={onConfirm}>
              Confirm
            </Button>
          </DialogActions>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default CreatePermissionModal;
