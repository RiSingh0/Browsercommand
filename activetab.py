from pywinauto import Application


def chrome_active_url():
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    element_name="Address and search bar"
    dlg = app.top_window()
    url = dlg.child_window(title=element_name, control_type="Edit").get_value()
    return(url)


def firefox_active_url():
    try:
        app = Application(backend='uia')
        app.connect(title_re=".*Mozilla Firefox.*",found_index=1)
        element_name="Search with Google or enter address"
        dlg = app.top_window()
        url = dlg.child_window(title=element_name, control_type="Edit").get_value()
        return(url)
    except:
        try:
            app = Application(backend='uia')
            app.connect(title_re=".*Mozilla Firefox.*",found_index=0)
            element_name="Search with Google or enter address"
            dlg = app.top_window()
            url = dlg.child_window(title=element_name, control_type="Edit").get_value()
            return(url)
        except:
            app = Application(backend='uia')
            app.connect(title_re=".*Mozilla Firefox.*")
            element_name="Search with Google or enter address"
            dlg = app.top_window()
            url = dlg.child_window(title=element_name, control_type="Edit").get_value()
            return(url)
