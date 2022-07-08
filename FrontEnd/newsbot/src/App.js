import "./App.css";
import NavbarComp from "./Components/Navbar";
import { Grid, Box } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { TextField } from "@mui/material";
import { Paper } from "@mui/material";
import { Button, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { myResults } from "./Components/Main Header";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

function App() {
  const [searchKeyword, setSearchKeyword] = useState("");
  const [result, setResult] = useState({});;

  const handleClick = (e) => {
    const tempResult = {
      message: searchKeyword,
    };
    myResults.push(tempResult);
    setResult(tempResult);
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <Grid container spacing={0.5} justifyContent="center" alignItems="center">
        <Grid item xs={12}>
          <NavbarComp />
        </Grid>
        <Grid item xs={6}>
          <Grid container sx={{ pt: 3 }} alignItems="center">
            <Box
              component="span"
              sx={{
                fontSize: 16,
                fontFamily: "Arial",
                fontWeight: "bold",
                mr: 2,
              }}
            >
              Please Enter a Query
            </Box>
            <Box sx={{ flexGrow: 1, mr: 1 }}>
              <Paper>
                <TextField
                  id="searchKeyword"
                  name="searchKeyword"
                  type="search"
                  variant="filled"
                  onChange={(v) => setSearchKeyword(v.target.value)}
                  fullWidth
                />
              </Paper>
            </Box>
            <Button onClick={handleClick} variant="contained">
              <Typography p={1}>Search</Typography>
            </Button>
          </Grid>
        </Grid>
        <Grid item xs={8}>
          <Grid container direction="column" sx={{ pt: 3 }} alignItems="center">
              {myResults.map((myVariable) => {
                return (
                  <Box
                    component="span"
                    sx={{
                      fontSize: 16,
                      fontFamily: "Arial",
                      fontWeight: "bold",
                      mr: 2,
                      flexGrow:1
                    }}
                  >
                    {myVariable.message}
                    {myVariable.name}
                  </Box>
                );
              })}
          </Grid>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}

export default App;
