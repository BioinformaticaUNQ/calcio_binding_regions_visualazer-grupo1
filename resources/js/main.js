var pdbFile = null;
const darkModIndicator = document.getElementById('darkIndicator');

const btnGenerateFASTA = document.getElementById('btnGenerateFASTA');
const btnOpenGraphic = document.getElementById('btnOpenGraphic');

window.lynxCBRV = {
    checkPDB: async () => {
      div = document.getElementById("pdbNotify");
      if(pdbFile == null){
        div.innerHTML=`
        <div class="info-box warning col-12" style="position:relative;">
          <div class="info-box-content">
            Remember, it is necessary to select a PDB file in order to verify it.
          </div>
        </div>
        `
      }else{
        let com = 'python3 resources/scripts/verify.py '.concat(pdbFile);
        let response = await Neutralino.os.execCommand({
          command: com
        });
        let resp = JSON.parse(response.output);
        if (resp.code == 200) {
          btnGenerateFASTA.disabled = false;
          div.innerHTML=`
          <div class="info-box success col-12" style="position:relative;">
            <div class="info-box-content">
              `.concat(resp.response).concat(`
            </div>
          </div>
          `)
        }else{
          div.innerHTML=`
          <div class="info-box alert col-12" style="position:relative;">
            <div class="info-box-content">
              `.concat(resp.response).concat(`
            </div>
          </div>
          `)
        }
      }
    },
    openPDB: async () => {
      let response = await Neutralino.os.showDialogOpen({
        title: 'Select Your PDB'
      });
      pdbFile = response.selectedEntry;
      setPathInfo();
    },
    openInPyMol : async () =>{
      let com = 'python3 resources/scripts/openPymol.py '.concat(pdbFile);
      let response = await Neutralino.os.execCommand({
        command: com
      });
    },
    clear : async () =>{
      await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/clear.py'
      });
      btnGenerateFASTA.disabled = true;
      btnOpenGraphic.disabled = true;
    },
    generateFasta: async () => {
      Metro.dialog.open("#fastaDialog");
      let com = 'python3 resources/scripts/getSecuencia.py '.concat(pdbFile);
      let response = await Neutralino.os.execCommand({
        command: com
      });
      btnOpenGraphic.disabled = false;
      Metro.dialog.close("#fastaDialog");
    },
    graficarFasta : async () =>{
      Metro.dialog.open("#graphicDialog");
      await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/graficarFasta.py'
      });
      Metro.dialog.close("#graphicDialog");
    },
    installReq : async () =>{
      Metro.dialog.open("#depDialog");
      await Neutralino.os.execCommand({
        command: 'pip3 install -r requisitos'
      });
      Metro.dialog.close("#depDialog");
    }
};

// Funciones

function setPathInfo(){
  div = document.getElementById("divFilePath");
  if (pdbFile) {
    div.value = pdbFile;
  }else{
    div.value = `You didn't select any file`;
    btnGenerateFASTA.disabled = true;
    btnOpenGraphic.disabled = true;
  }
}

function toggleDarkMode(){
  if (darkIndicator.checked) {
    document.documentElement.style.setProperty('--bg-color', 'rgba(0,0,0,0.85)');
    document.documentElement.style.setProperty('--font-color', '#FFF');
  }else {
    document.documentElement.style.setProperty('--bg-color', 'rgba(255,255,255,0.85)');
    document.documentElement.style.setProperty('--font-color', '#000');
  }
}

function changePrimaryColor(color){
  document.documentElement.style.setProperty('--primary-color', String(color));
}

// Secuencia de inicio
Neutralino.init();
setPathInfo();
btnGenerateFASTA.disabled = true;
btnOpenGraphic.disabled = true;
window.lynxCBRV.clear();
