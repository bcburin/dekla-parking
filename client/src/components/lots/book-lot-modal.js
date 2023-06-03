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
import { ErrorMessage, Field, Form, Formik, useFormik } from "formik";
import { useDispatch, useSelector } from "react-redux";

import React from "react";
import { actions } from "src/store/lot-ui-slice";
import lotsAPI from "src/api/lots";

const BookLotModal = () => {
  const dispatch = useDispatch();
  const bookLotModalIsOpen = useSelector(
    (store) => store.lotUI.bookLotModalIsOpen
  );
  const selectedLot = useSelector((store) => store.lotUI.selectedLot);

  const formik = useFormik({
    initialValues: {
      startTime: "",
      endTime: "",
    },
    validationSchema: Yup.object({
      startTime: Yup.date().required("Start time is required"),
      endTime: Yup.date()
        .required("End time is required")
        .min(Yup.ref("startTime"), "End time must be after start time"),
    }),
    onSubmit: async (values, helpers) => {
      try {
        await lotsAPI.bookForMe(selectedLot.id, values);
      } catch {
        helpers.setStatus({ success: false });
        helpers.setErrors({ submit: err.message });
        helpers.setSubmitting(false);
      } finally {
        dispatch(actions.closeBookLotModal());
      }
    },
  });

  return (
    selectedLot && (
      <Dialog open={bookLotModalIsOpen}>
        <DialogTitle>Book Parking Lot</DialogTitle>
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
            </Stack>
            {formik.errors.submit && (
              <Typography color="error" sx={{ mt: 3 }} variant="body2">
                {formik.errors.submit}
              </Typography>
            )}
            <DialogActions>
              <Button onClick={() => dispatch(actions.closeBookLotModal())}>
                Cancel
              </Button>
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

export default BookLotModal;
