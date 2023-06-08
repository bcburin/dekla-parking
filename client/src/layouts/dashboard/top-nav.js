import {
  Avatar,
  Badge,
  Box,
  IconButton,
  Stack,
  SvgIcon,
  Tooltip,
  useMediaQuery,
  useTheme,
} from "@mui/material";

import { AccountPopover } from "./account-popover";
import Bars3Icon from "@heroicons/react/24/solid/Bars3Icon";
import BellIcon from "@heroicons/react/24/solid/BellIcon";
import MagnifyingGlassIcon from "@heroicons/react/24/solid/MagnifyingGlassIcon";
import PropTypes from "prop-types";
import UsersIcon from "@heroicons/react/24/solid/UsersIcon";
import { alpha } from "@mui/material/styles";
import { usePopover } from "src/hooks/use-popover";
import { useSelector } from "react-redux";

const SIDE_NAV_WIDTH = 280;
const TOP_NAV_HEIGHT = 64;

export const TopNav = (props) => {
  const { onNavOpen } = props;
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up("lg"));
  const accountPopover = usePopover();
  const loggedUser = useSelector((store) => store.auth.loggedUser);
  const theme = useTheme();

  return (
    loggedUser && (
      <>
        <Box
          component="header"
          sx={{
            backdropFilter: "blur(6px)",
            backgroundColor: (theme) =>
              alpha(theme.palette.background.default, 0.8),
            position: "sticky",
            left: {
              lg: `${SIDE_NAV_WIDTH}px`,
            },
            top: 0,
            width: {
              lg: `calc(100% - ${SIDE_NAV_WIDTH}px)`,
            },
            zIndex: (theme) => theme.zIndex.appBar,
          }}
        >
          <Stack
            alignItems="center"
            direction="row"
            justifyContent="space-between"
            spacing={2}
            sx={{
              minHeight: TOP_NAV_HEIGHT,
              px: 2,
            }}
          >
            <Stack alignItems="center" direction="row" spacing={2}>
              {!lgUp && (
                <IconButton onClick={onNavOpen}>
                  <SvgIcon fontSize="small">
                    <Bars3Icon />
                  </SvgIcon>
                </IconButton>
              )}
            </Stack>
            <Stack alignItems="center" direction="row" spacing={2}>
              <Avatar
                onClick={accountPopover.handleOpen}
                ref={accountPopover.anchorRef}
                sx={{
                  cursor: "pointer",
                  height: 40,
                  width: 40,
                  bgcolor: theme.palette.primary.dark,
                }}
              >
                {loggedUser.firstName.charAt(0) + loggedUser.lastName.charAt(0)}
              </Avatar>
            </Stack>
          </Stack>
        </Box>
        <AccountPopover
          anchorEl={accountPopover.anchorRef.current}
          open={accountPopover.open}
          onClose={accountPopover.handleClose}
        />
      </>
    )
  );
};

TopNav.propTypes = {
  onNavOpen: PropTypes.func,
};
