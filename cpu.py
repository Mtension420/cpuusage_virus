import multiprocessing

def cpu_intensive_task():
    while True:
        [x**2 for x in range(10000)]

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()  # Use all available CPU cores

    # Create and start processes
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_intensive_task)
        processes.append(process)
        process.start()

    # Keep the main process alive
    for process in processes:
        process.join()
