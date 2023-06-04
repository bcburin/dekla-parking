import * as Yup from "yup";

import { Stack, TextField, Typography } from "@mui/material";

import Button from "@mui/material/Button";
import { ChromePicker } from "react-color";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import labelsAPI from "src/api/labels";
import { useFormik } from "formik";

const CreateLabelModal = ({ open, onClose, onConfirm }) => {
  const formik = useFormik({
    initialValues: {
      name: "",
      description: "",
      priority: 0,
      color: "#DDD",
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
        await labelsAPI.createEntity(values);
        await onConfirm();
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
      <DialogTitle>Create Label</DialogTitle>
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
            <Typography variant="body1">Color</Typography>
            <ChromePicker
              color={formik.values.color}
              onChange={handleColorChange}
              disableAlpha={true}
            />
          </Stack>
          {formik.errors.submit && (
            <Typography color="error" sx={{ mt: 3 }} variant="body2">
              {formik.errors.submit}
            </Typography>
          )}
          <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button variant="contained" color="error" type="submit">
              Create
            </Button>
          </DialogActions>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default CreateLabelModal;
