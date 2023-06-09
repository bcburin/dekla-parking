import * as Yup from "yup";

import { Stack, TextField, Typography } from "@mui/material";

import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import sectorAPI from "src/api/sectors";
import { useFormik } from "formik";

const EditSectorModal = ({ open, onClose, onConfirm, sector }) => {
  const formik = useFormik({
    initialValues: {
      name: sector?.name || "",
      description: sector?.description || "",
      submit: null,
    },
    validationSchema: Yup.object({
      name: Yup.string().max(255),
      description: Yup.string().max(255),
    }),
    onSubmit: async (values, helpers) => {
      try {
        await sectorAPI.updateEntity(sector.id, values);
        await onConfirm();
      } catch (err) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
      }
    },
  });

  return (
    sector && (
      <Dialog open={open} onClose={onClose}>
        <DialogTitle>Update Policy</DialogTitle>
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
            </Stack>
            {formik.errors.submit && (
              <Typography color="error" sx={{ mt: 3 }} variant="body2">
                {formik.errors.submit}
              </Typography>
            )}
            <DialogActions>
              <Button onClick={onClose}>Cancel</Button>
              <Button variant="contained" color="error" type="submit">
                Update
              </Button>
            </DialogActions>
          </form>
        </DialogContent>
      </Dialog>
    )
  );
};

export default EditSectorModal;
