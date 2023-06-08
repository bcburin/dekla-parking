import * as Yup from "yup";

import { Form, Formik } from "formik";
import { Stack, TextField, Typography } from "@mui/material";

import Button from "@mui/material/Button";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import userAPI from "src/api/users";

const UpdateUserForm = ({ title, user }) => {
  const initialValues = {
    email: user.email,
    firstName: user.firstName,
    lastName: user.lastName,
    password: "",
  };

  const validationSchema = Yup.object({
    email: Yup.string().email("Must be a valid email").max(255),
    firstName: Yup.string().max(255),
    lastName: Yup.string().max(255),
    password: Yup.string().max(255),
  });

  const handleSubmit = async (values, helpers) => {
    try {
      await userAPI.updateEntity(user.id, values);
    } catch (err) {
      helpers.setStatus({ success: false });
      helpers.setErrors({ submit: err.message });
      helpers.setSubmitting(false);
    }
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      {(formik) => (
        <Form noValidate>
          {title && <DialogTitle>{title}</DialogTitle>}
          <DialogContent>
            <Stack spacing={3}>
              <TextField
                error={!!(formik.touched.firstName && formik.errors.firstName)}
                fullWidth
                helperText={formik.touched.firstName && formik.errors.firstName}
                label="First Name"
                name="firstName"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                value={formik.values.firstName}
              />
              <TextField
                error={!!(formik.touched.lastName && formik.errors.lastName)}
                fullWidth
                helperText={formik.touched.lastName && formik.errors.lastName}
                label="Last Name"
                name="lastName"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                value={formik.values.lastName}
              />
              <TextField
                error={!!(formik.touched.email && formik.errors.email)}
                fullWidth
                helperText={formik.touched.email && formik.errors.email}
                label="Email Address"
                name="email"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                type="email"
                value={formik.values.email}
              />
              <TextField
                error={!!(formik.touched.password && formik.errors.password)}
                fullWidth
                helperText={formik.touched.password && formik.errors.password}
                label="Password"
                name="password"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                type="password"
                value={formik.values.password}
              />
            </Stack>
            {formik.errors.submit && (
              <Typography color="error" sx={{ mt: 3 }} variant="body2">
                {formik.errors.submit}
              </Typography>
            )}
          </DialogContent>
          <DialogActions>
            <Button
              variant="contained"
              color="error"
              type="submit"
              disabled={formik.isSubmitting || !formik.isValid}
            >
              Update
            </Button>
          </DialogActions>
        </Form>
      )}
    </Formik>
  );
};

export default UpdateUserForm;
