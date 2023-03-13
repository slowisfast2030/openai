pragma solidity ^0.8.0;

// ERC20代币标准

interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// ERC20代币实现

contract MyToken is IERC20 {
    string public constant name = "My Token";        // 代币名称
    string public constant symbol = "MYT";           // 代币符号
    uint8 public constant decimals = 18;             // 精度设置为18位小数
    uint256 private constant _totalSupply = 1000000; // 代币总量
    
    mapping (address => uint256) private _balances;            // 存储每个用户的代币余额
    mapping (address => mapping (address => uint256)) private _allowances;  // 存储每个地址允许发送给其他地址的代币数量
    
    constructor() {
        _balances[msg.sender] = _totalSupply;
    }
    
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }
    
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_balances[msg.sender] >= amount, "ERC20: insufficient balance");
        
        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        
        emit Transfer(msg.sender, recipient, amount);
        
        return true;
    }
    
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
    
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        
        emit Approval(msg.sender, spender, amount);
        
        return true;
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_balances[sender] >= amount, "ERC20: insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "ERC20: insufficient allowance");
        
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        
        emit Transfer(sender, recipient, amount);
        
        return true;
    }
}
