// import * as React from "react";
// import AppBar from "@mui/material/AppBar";
// import Toolbar from "@mui/material/Toolbar";
// import Typography from "@mui/material/Typography";
// import { Grid } from "@mui/material";
// import IconButton from "@mui/material/IconButton";
// import AccountCircle from "@mui/icons-material/AccountCircle";
// import {Box} from "@mui/material";

// const NavbarComp = () => {
//   return (
//     <Box sx={{ flexGrow: 1 }}>
//       <AppBar position="static">
//         <Grid container maxWidth="xl" alignItems="center">
//           <Toolbar disableGutters>
//             <Typography
//               variant="h3"
//               noWrap
//               component="div"
//               href="/"
//               sx={{
//                 mr: 2,
//                 display: { xs: "none", md: "flex" },
//                 fontFamily: "monospace",
//                 fontWeight: 700,
//                 letterSpacing: ".3rem",
//                 color: "inherit",
//                 textDecoration: "none",
//                 flexGrow: 1,
//               }}
//             >
//               NewsBot
//             </Typography>
//             <IconButton
//               size="large"
//               aria-label="account of current user"
//               aria-controls="menu-appbar"
//               aria-haspopup="true"
//               color="inherit"
//             >
//               <AccountCircle />
//             </IconButton>
//           </Toolbar>
//         </Grid>
//       </AppBar>
//     </Box>
//   );
// };
// export default NavbarComp;




import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

export default function NavbarComp() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography
              variant="h3"
              noWrap
              component="div"
              href="/"
              sx={{
                mr: 2,
                display: { xs: "none", md: "flex" },
                fontFamily: "monospace",
                fontWeight: 700,
                letterSpacing: ".3rem",
                color: "inherit",
                textDecoration: "none",
                flexGrow: 1,
              }}
            >
              NewsBot
            </Typography>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
