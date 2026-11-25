const videoPreview = document.querySelector('.video-preview');
videoPreview.addEventListener('click', event => {
  if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
  event.preventDefault();
  const frame = videoPreview.parentElement.querySelector('template').content.firstElementChild.cloneNode(true);
  videoPreview.replaceWith(frame);
  frame.focus();
});
