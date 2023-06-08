import * as Yup from "yup";

import { Stack, TextField, Typography } from "@mui/material";

import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import { useFormik } from "formik";

const UpdatePolicyModal = ({ open, onClose, onConfirm, policyData, api }) => {
  const formik = useFormik({
    initialValues: {
      name: policyData?.name || "",
      descriptor: policyData?.descriptor || "",
      price: policyData?.price || 0,
      submit: null,
    },
    validationSchema: Yup.object({
      name: Yup.string().max(255),
      descriptor: Yup.string().max(255),
      price: Yup.number().min(0),
    }),
    onSubmit: async (values, helpers) => {
      try {
        await api.updateEntity(policyData.id, values); // Call the appropriate API endpoint for updating the policy
        await onConfirm();
      } catch (err) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
      }
    },
  });

  return (
    policyData && (
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
                  !!(formik.touched.descriptor && formik.errors.descriptor)
                }
                fullWidth
                multiline
                rows={4}
                helperText={
                  formik.touched.descriptor && formik.errors.descriptor
                }
                label="Description"
                name="descriptor"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                value={formik.values.descriptor}
              />
              <TextField
                error={!!(formik.touched.price && formik.errors.price)}
                fullWidth
                helperText={formik.touched.price && formik.errors.price}
                label="Price"
                name="price"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                type="number"
                value={formik.values.price}
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

export default UpdatePolicyModal;
