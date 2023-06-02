import * as Yup from "yup";

import {
  Stack,
  TextField,
  Typography,
  FormControlLabel,
  Checkbox,
} from "@mui/material";

import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { useFormik } from "formik";
import lotsAPI from "src/api/lots";

const CreateLotModal = ({ open, onClose, onConfirm, onRefresh, sector }) => {
  const formik = useFormik({
    initialValues: {
      name: "",
      location: "",
      description: "",
      available: true,
      submit: null,
    },
    validationSchema: Yup.object({
      name: Yup.string().max(255).required("Name is required"),
      location: Yup.string().max(255).required("Location is required"),
      description: Yup.string().max(255),
      available: Yup.bool(),
    }),
    onSubmit: async (values, helpers) => {
      try {
        const createdLot = await lotsAPI.createEntity(values);
        if (sector) await lotsAPI.assign(createdLot.id, sector.id);
        await onRefresh();
      } catch (err) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
      }
    },
  });

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Create Lot</DialogTitle>
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
              value={formik.values.firstName}
            />
            <TextField
              error={!!(formik.touched.location && formik.errors.location)}
              fullWidth
              helperText={formik.touched.location && formik.errors.location}
              name="location"
              label="Location"
              type="text"
              margin="normal"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              value={formik.values.location}
            />
            <TextField
              error={!!(formik.touched.email && formik.errors.email)}
              fullWidth
              multiline
              rows={4}
              helperText={formik.touched.email && formik.errors.email}
              label="Description"
              name="description"
              onBlur={formik.handleBlur}
              onChange={formik.handleChange}
              value={formik.values.email}
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={formik.values.available}
                  onChange={formik.handleChange}
                  name="available"
                />
              }
              label="Available"
            />
          </Stack>
          {formik.errors.submit && (
            <Typography color="error" sx={{ mt: 3 }} variant="body2">
              {formik.errors.submit}
            </Typography>
          )}
          <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button
              onClick={onConfirm}
              variant="contained"
              color="error"
              type="submit"
            >
              Create
            </Button>
          </DialogActions>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default CreateLotModal;
