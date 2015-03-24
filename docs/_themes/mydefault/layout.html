{#
    default/layout.html
    ~~~~~~~~~~~~~~~~~~~

    Sphinx layout template for the default theme.

    :copyright: Copyright 2007-2014 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
#}
{%- extends "basic/layout.html" %}

{% macro comments() %}
    <div id="disqus_thread"></div>
    <script type="text/javascript">
    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'wwwlectures'; // required: replace example with your forum shortname
    {% trans pagename=pagename|e %}var disqus_identifier = '{{ pagename }}';{% endtrans %}
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
{% endmacro %}

{% if theme_collapsiblesidebar|tobool %}
    {% set script_files = script_files + ['_static/sidebar.js'] %}
{% endif %}

{% block content %}

    <script type="text/javascript">
        $(document).ready(function() {
            // TODO: SVG not work
            $(".image-reference").fancybox({});
        });
    </script>

    {{ super() }}
    {%- if not internal_build and (pagename != 'index') %}
      <hr/>
      {{ comments() }}
    {%- endif %}
{% endblock %}
