import {
  Avatar,
  Box,
  Button,
  Card,
  CardActions,
  CardContent,
  Divider,
  Typography,
  useTheme,
} from "@mui/material";
import { useSelector } from "react-redux";

export const AccountProfile = () => {
  const loggedUser = useSelector((store) => store.auth.loggedUser);
  const theme = useTheme();

  return (
    <Card>
      <CardContent>
        <Box
          sx={{
            alignItems: "center",
            display: "flex",
            flexDirection: "column",
          }}
        >
          <Avatar
            sx={{
              height: 200,
              mb: 2,
              width: 200,
              fontSize: 64,
              bgcolor: theme.palette.primary.dark,
            }}
          >
            {loggedUser.firstName.charAt(0) + loggedUser.lastName.charAt(0)}
          </Avatar>
          <Typography gutterBottom variant="h5">
            {`${loggedUser.firstName} ${loggedUser.lastName}`}
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
};
