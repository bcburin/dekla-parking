import {
  Box,
  Divider,
  MenuItem,
  MenuList,
  Popover,
  Typography,
} from "@mui/material";
import { useDispatch, useSelector } from "react-redux";

import PropTypes from "prop-types";
import { logout } from "src/store/auth-actions";
import { useCallback } from "react";
import { useRouter } from "next/navigation";

export const AccountPopover = (props) => {
  const dispatch = useDispatch();
  const { anchorEl, onClose, open } = props;
  const router = useRouter();
  const loggedUser = useSelector((store) => store.auth.loggedUser);

  const handleSignOut = useCallback(() => {
    onClose?.();
    dispatch(logout());
    router.push("/auth/login");
  }, [onClose, router]);

  return (
    loggedUser && (
      <Popover
        anchorEl={anchorEl}
        anchorOrigin={{
          horizontal: "left",
          vertical: "bottom",
        }}
        onClose={onClose}
        open={open}
        PaperProps={{ sx: { width: 200 } }}
      >
        <Box
          sx={{
            py: 1.5,
            px: 2,
          }}
        >
          <Typography variant="overline">Account</Typography>
          <Typography color="text.secondary" variant="body2">
            {`${loggedUser.firstName} ${loggedUser.lastName}`}
          </Typography>
        </Box>
        <Divider />
        <MenuList
          disablePadding
          dense
          sx={{
            p: "8px",
            "& > *": {
              borderRadius: 1,
            },
          }}
        >
          <MenuItem onClick={handleSignOut}>Sign out</MenuItem>
        </MenuList>
      </Popover>
    )
  );
};

AccountPopover.propTypes = {
  anchorEl: PropTypes.any,
  onClose: PropTypes.func,
  open: PropTypes.bool.isRequired,
};
