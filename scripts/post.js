/* eslint-env jquery */
/* global marked, PR */
(function () {
  function initialiseMarkdown () {
    'use strict'
    $('.post__content > div').each(function () {
      var $this = $(this)
      var content = $this.text()
      var markedContent = marked(content)
      $this.html(markedContent)
      $this.find('pre').addClass('prettyprint linenums')
    })

    PR.prettyPrint()
  }

  $(function () {
    initialiseMarkdown()
  })
})()
