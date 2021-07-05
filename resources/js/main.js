var pdbFile = null;

window.lynxCBRV = {
    showInfo: () => {
      document.getElementById('info').innerHTML = NL_APPID + " is running on port " +
                  NL_PORT + " inside " + NL_OS + ".<br/><br/>" + "<span>v" + NL_VERSION + "</span>";
    },
    openDocs: () => {
      Neutralino.app.open({
        url: "https://neutralino.js.org/docs"
      });
    },
    checkPDB: () => {
      if(pdbFile == null){
        // Por favor seleccione un PDB
      }else{
        // Existe File
      }
    },
    openPDB: async () => {
      let response = await Neutralino.os.showDialogOpen({
        title: 'Select Your PDB'
      });
      pdbFile = response.selectedEntry;
      setPathInfo();
    }
};

// Funciones

function setPathInfo(){
  div = document.getElementById("divFilePath");
  if (pdbFile) {
    div.value = pdbFile;
  }else{
    div.value = `You didn't select any file`;
  }
}

// Secuencia de inicio

Neutralino.init();
setPathInfo();
