import cx_Freeze


executables = [cx_Freeze.Executable("__main__.py")]

cx_Freeze.setup(
    name="Chess Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[""]}},
    executables = executables

    )
