{


  const file = document.getElementById('file');
  const fileInputImg = document.querySelector('.file_input_img');
  const fileInputMessage = document.querySelector('.file_input_message');
  file.addEventListener('change', (e) => {
    if (!e.target.files[0]) {
      fileInputImg.style.display = 'none';
      fileInputMessage.style.display = 'block';
    } else {
      fileInputImg.style.display = 'block';
      fileInputImg.src = window.URL.createObjectURL(e.target.files[0]);
      fileInputMessage.style.display = 'none';
    }
  });

  const btn = document.getElementById('btn');
  const uploading = () => {
    btn.textContent = '作成中...';
    btn.disabled = true;
  }

  const keyword = document.getElementById('keyword');
  const fileName = document.getElementById('file_name');
  const uploaded = () => {
    btn.disabled = false;
    btn.textContent = '作成';
    keyword.value = '';
    file.value = '';
    fileName.value = '';
    fileInputImg.style.display = 'none';
    fileInputMessage.style.display = 'block';
    alert('作成が完了しました。');
  }

  const form = document.getElementById('form');
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    uploading();
    let fd = new FormData();
    fd.append('keyword', keyword.value);
    fd.append('file', file.files[0]);
    fd.append('fileName', fileName.value);

    fetch('/upload', {
      method: 'POST',
      body: fd
    })
    .then(res => res.json())
    .then(data => {
      if (data.result) {
        uploaded();
      } else {
        alert(data.message);
        btn.disabled = false;
        btn.textContent = '作成';
      }
    });
  });



}



