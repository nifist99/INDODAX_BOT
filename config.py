from api.web import tanlalana



class setting:
        def __init__(self,id_users):
    #key dari indodax
            self.id_users = id_users
      
        def screetkey(self):
            global screetkey
            screetkey=tanlalana.indodax_setting("screetkey",self.id_users)
            return screetkey['parameter_text']

        #apikey dari web
        def apikey(self):
            global apikey
            apikey=tanlalana.indodax_setting("apikey",self.id_users)
            return apikey['parameter_text']

#windows not sleep
class WindowsInhibitor:
        '''Prevent OS sleep/hibernate in windows; code from:
        https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/preventsuspendplus/core.py
        API documentation:
        https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx'''
        ES_CONTINUOUS = 0x80000000
        ES_SYSTEM_REQUIRED = 0x00000001

        def __init__(self):
            pass

        def inhibit(self):
            import ctypes
            print("")
            print("")
            print("======================================")
            print("Inisialisasi..........................")
            print("Preventing Windows from going to sleep")
            ctypes.windll.kernel32.SetThreadExecutionState(
                WindowsInhibitor.ES_CONTINUOUS | \
                WindowsInhibitor.ES_SYSTEM_REQUIRED)

        def uninhibit(self):
            import ctypes
            print("Allowing Windows to go to sleep")
            ctypes.windll.kernel32.SetThreadExecutionState(
                WindowsInhibitor.ES_CONTINUOUS)