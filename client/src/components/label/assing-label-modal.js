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

import labelsAPI from "src/api/labels";
import { useFormik } from "formik";
import userAPI from "src/api/users";

const AssignLabelModal = ({ label, open, onClose, onConfirm }) => {
  const [users, setUsers] = useState([]);

  const getUsers = async () => {
    try {
      const users = await userAPI.getEntities();
      setUsers(users);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getUsers();
  }, []);

  const formik = useFormik({
    initialValues: {
      startTime: "",
      endTime: "",
      user: null,
    },
    validationSchema: Yup.object({
      startTime: Yup.date(),
      endTime: Yup.date().min(
        Yup.ref("startTime"),
        "End time must be after start time"
      ),
    }),
    onSubmit: async (values, helpers) => {
      try {
        await labelsAPI.assignToUser(label.id, values.user.id, {
          startTime: values.startTime || null,
          endTime: values.endTime || null,
        });
        if (onConfirm) onConfirm();
      } catch (e) {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: e.response?.data?.detail || e.message });
        helpers.setSubmitting(false);
      }
    },
  });

  return (
    label && (
      <Dialog open={open}>
        <DialogTitle>Assign Label to User</DialogTitle>
        <DialogContent>
          <form noValidate onSubmit={formik.handleSubmit}>
            <Stack spacing={3}>
              <Autocomplete
                options={users}
                getOptionLabel={(user) =>
                  user?.firstName +
                    " " +
                    user?.lastName +
                    ` [${user?.username}]` || ""
                }
                renderInput={(params) => (
                  <TextField
                    {...params}
                    label="Select a User"
                    fullWidth
                    autoFocus
                    error={!!(formik.touched.user && formik.errors.user)}
                    helperText={formik.touched.user && formik.errors.user}
                    value={formik.values.user}
                    onBlur={formik.handleBlur}
                    InputLabelProps={{
                      shrink: true,
                    }}
                  />
                )}
                onInputChange={(event, value) => {
                  const selectedUser = users.find(
                    (user) =>
                      user?.firstName +
                        " " +
                        user?.lastName +
                        ` [${user?.username}]` ===
                      value
                  );
                  formik.setFieldValue("user", selectedUser);
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
    )
  );
};

export default AssignLabelModal;
