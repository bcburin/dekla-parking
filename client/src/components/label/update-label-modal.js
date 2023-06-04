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

import { ChromePicker } from "react-color";
import labelsAPI from "src/api/labels";
import { useFormik } from "formik";

const UpdateLabelModal = ({ open, onClose, onConfirm, label }) => {
  const formik = useFormik({
    initialValues: {
      name: label.name || "",
      description: label.description || "",
      priority: label.priority || 0,
      color: label.color || "#DDD",
      submit: null,
    },
    validationSchema: Yup.object({
      name: Yup.string().max(255).required("Name is required"),
      description: Yup.string().max(255),
      priority: Yup.number().integer().min(0).required("Priority is required"),
      color: Yup.string().nullable().required("Color is required"),
    }),
    onSubmit: async (values, helpers) => {
      try {
        const updatedLabel = await labelsAPI.updateEntity(label.id, values);
        if (updatedLabel) await onConfirm(updatedLabel);
      } catch (err) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
      }
    },
  });

  const handleColorChange = (color) => {
    formik.setFieldValue("color", color.hex);
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Update Label</DialogTitle>
      <DialogContent>
        <form noValidate onSubmit={formik.handleSubmit}>
          <Stack spacing={3}>
            <TextField
              error={!!(formik.touched.name && formik.errors.name)}
              fullWidth
              helperText={formik.touched.name && formik.errors.name}
              label="Name"
              name="name"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              value={formik.values.name}
            />
            <TextField
              error={
                !!(formik.touched.description && formik.errors.description)
              }
              fullWidth
              multiline
              rows={4}
              helperText={
                formik.touched.description && formik.errors.description
              }
              label="Description"
              name="description"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              value={formik.values.description}
            />
            <Typography variant="body1">Color</Typography>
            <ChromePicker
              color={formik.values.color}
              onChange={handleColorChange}
              disableAlpha
            />
            <TextField
              error={!!(formik.touched.priority && formik.errors.priority)}
              fullWidth
              helperText={formik.touched.priority && formik.errors.priority}
              label="Priority"
              name="priority"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              type="number"
              value={formik.values.priority}
            />
          </Stack>
          {formik.errors.submit && (
            <Typography color="error" sx={{ mt: 3 }} variant="body2">
              {formik.errors.submit}
            </Typography>
          )}
          <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button variant="contained" color="primary" type="submit">
              Save
            </Button>
          </DialogActions>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default UpdateLabelModal;
