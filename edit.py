                <link rel="stylesheet" data-name="vs/editor/editor.main" href="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/editor/editor.main.min.css">
                <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/loader.min.js"></script>
                <hr class="main_hr">
                <form method="post">
                    <script>
                        do_stop_exit()
                        var editor_value = 0;
                        
                        require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs' }});
                        require(["vs/editor/editor.main"], function () {
                            window.editor = monaco.editor.create(document.getElementById('monaco_editor'), {
                                value: document.getElementById('content').value,
                                language: 'plaintext',
                                theme: 'vs',
                                wordWrap: true
                            });
                        });
                        
                        function monaco_to_content() {
                            var normal = document.getElementById("content");
                            var monaco = document.getElementById("monaco_editor");
                            if (normal.style.display == "none") {
                                document.getElementById('content').value = window.editor.getValue();
                            }
                        }
                        
                        function content_to_monaco() {
                                var e      = document.querySelector('#content');
                                var monaco = document.querySelector('#monaco_editor');
                                monaco.style.display == 'none' ? editor.setValue(e.value) : 0;
                        }
                        
                        function change_editor() {
                            var normal = document.getElementById("content");
                            var monaco = document.getElementById("monaco_editor");
                            if (normal.style.display == "none") {
                                normal.style.display = "block";
                                monaco.style.display = "none";
                                document.getElementById("editor").innerHTML = "모나코 편집기";
                                editor_value = 1;
                            } else {
                                normal.style.display = "none";
                                monaco.style.display = "block";
                                document.getElementById("editor").innerHTML = "기본 편집기";
                                editor_value = 0;
                            }
                        }
                        
                        function change_preview() {
                            var normal = document.getElementById("content");
                            var monaco = document.getElementById("monaco_editor");
                            var preview = document.getElementById("see_preview");
                            if (preview.style.display == "none") {
                                preview.style.display = "block";
                                normal.style.display = "none";
                                monaco.style.display = "none";
                                document.getElementById("preview").innerHTML = "편집기 열기";
                            } else if (preview.style.display == "block" && editor_value == 0) {
                                preview.style.display = "none";
                                normal.style.display = "none";
                                monaco.style.display = "block";
                                document.getElementById("preview").innerHTML = "미리보기";
                            } else {
                                preview.style.display = "none";
                                normal.style.display = "block";
                                monaco.style.display = "none";
                                document.getElementById("preview").innerHTML = "미리보기";
                            }
                        }
                    </script>
                    <style>
                        #monaco_editor { height: 500px; }
                        #content { height: 500px; }
                        #see_preview { height: 500px; overflow-y: scroll; }
                    </style>
                    <div ''' + editor_display + '''>''' + edit_button() + '''</div>
                    <div id="monaco_editor" class="content" ''' + monaco_display + '''></div>
                    <textarea id="content" ''' + editor_display + ''' class="content" name="content">''' + html.escape(re.sub('\n$', '', data)) + '''</textarea>
                    <div id="see_preview" style="display: none"></div>
                    <hr class="main_hr">
                    <input placeholder="''' + load_lang('why') + '''" name="send" type="text">
                    <textarea id="origin" name="otent">''' + html.escape(re.sub('\n$', '', data_old)) + '''</textarea>
                    <hr class="main_hr">
                    ''' + captcha_get() + ip_warring() + '''
                    <hr class="main_hr">
                    <button id="save" type="submit" onclick="monaco_to_content();">''' + load_lang('save') + '''</button>
                    <button id="preview" type="button" onclick="monaco_to_content(); change_preview(); load_preview(\'''' + url_pas(name) + '\')''''">''' + load_lang('preview') + '''</button>
                    <button id="editor" type="button" onclick="monaco_to_content(); change_editor();" style="float: right">기본 편집기</button>
                </form>
                <hr class="main_hr">
                <div id="include_1"></div>
 
