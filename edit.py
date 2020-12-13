        return easy_minify(flask.render_template(skin_check(), 
            imp = [name, wiki_set(), custom(), other2([' (' + sub + ')', 0])],
            data = '''
                <link rel="stylesheet" data-name="vs/editor/editor.main" href="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/editor/editor.main.min.css">
                <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/loader.min.js"></script>
                <hr class="main_hr">
                <form method="post">
                    <div id="wiki_notice">편집기가 대폭 개편되었습니다. 헷갈리는 경우 도움말을 반드시 확인해주세요.</strong> <details><summary>도움말 확인</summary><li>기본 편집기 버튼을 눌러서 모나코 에디터에서 기본 편집기로 변경할 수 있습니다.</li><li>다시 모나코 편집기를 눌러 기본 편집기에서 모나코 편집기로 변경할 수 있습니다.</li><li>모나코 편집기 > 기본 편집기로 넘어가는 경우, 모나코 편집기에 있던 내용이 기본 편집기로 자동으로 이동합니다.</li><li>하지만 기본 편집기에 있던 내용은 모나코 편집기로 바꿔도 다시 넘어오지 않습니다.</li><li>또한 <strong>한 번 기본 편집기로 전환한 경우</strong>, 모든 저장 내용은 <strong>기본 편집기를 기준으로 이루어집니다.</strong> (모나코 편집기에 내용을 입력해도 저장 시에는 기본 편집기에 있는 내용으로 저장됨)</li></details></div>
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
                    <label>저장 버튼을 누르게 되면 당신은 기여한 내용을 <strong>CC BY-NC-SA 2.0 KR</strong>으로 배포하고, 바다위키의 기본 규정을 준수하며 기여한 문서에 대한 하이퍼링크나 URL을 이용하여 저작자 표시를 하는 것으로 충분하다는 데 동의하는 것입니다. 이 <strong>동의는 철회할 수 없습니다.</strong></label>
                    ''' + captcha_get() + ip_warring() + '''
                    <hr class="main_hr">
                    <button id="save" type="submit" onclick="monaco_to_content();">''' + load_lang('save') + '''</button>
                    <button id="preview" type="button" onclick="monaco_to_content(); change_preview(); load_preview(\'''' + url_pas(name) + '\')''''">''' + load_lang('preview') + '''</button>
                    <button id="editor" type="button" onclick="monaco_to_content(); change_editor();" style="float: right">기본 편집기</button>
                </form>
                <hr class="main_hr">
                <div id="include_1"></div>
                <script>load_include("틀:바다위키", "include_1", []);</script>
            ''',
            menu = [['backlink/' + url_pas(name), load_lang('backlink')], ['delete/' + url_pas(name), load_lang('delete')], ['move/' + url_pas(name), load_lang('move')]]
        ))
