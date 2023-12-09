document.getElementById("captureButton").addEventListener("click", function() {

    // Запрос разрешения на захват экрана
navigator.mediaDevices.getDisplayMedia({ video: true })
.then((stream) => {
  // Создание видео элемента и передача потока экрана
  const video = document.createElement('video');
  video.srcObject = stream;
  video.autoplay = true;

  // Обработчик события play
  video.addEventListener('play', () => {
    // Создание холста
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Получение контекста рисования холста
    const context = canvas.getContext('2d');
    if (!context) {
      throw new ReferenceError("Element 'context' isn't defined.");
    }

    // Рисование текущего кадра видео на холсте
    context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    // Создание якоря для скачивания
    const a = document.createElement('a');
    a.download = `${new Date().toLocaleString()}.png`;
    a.href = canvas.toDataURL();
    a.click();

    // Освобождение ресурсов
    URL.revokeObjectURL(a.href);
    a.remove();
    canvas.remove();
    video.remove();
    stream.getTracks().forEach(track => track.stop());
  });
})
.catch((reason) => {
  console.error(reason instanceof Error ? reason : new Error(reason));
});

});
