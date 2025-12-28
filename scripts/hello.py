import torch

def main():
    print("Hello from flake-finder!")
    print("torch:", torch.__version__)
    print("cuda available:", torch.cuda.is_available())

if __name__ == "__main__":
    main()
