#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class TreeNode{
    public:
        int depth;
        vector<int> val;
        TreeNode* right = nullptr;
        TreeNode* left = nullptr;

        TreeNode(){
            
        }
        TreeNode(vector<int> val){
            this->val = val;
        }
        TreeNode(vector<int> val, int depth){
            this->depth = depth;
            this->val = val;
        }
};

void display(TreeNode* head){

}

TreeNode* insertion(TreeNode* head,int k){
    cout<<" creating a new node "<<endl;
    vector<int> val(k, 0);
    for(int i = 0; i <k ;i++){
        cin>>val[i];
    }
    TreeNode *newNode = new TreeNode(val);
    cout<<" new node is created "<<endl;
    int depth = 0;
    TreeNode *temp = head;
    if(temp == nullptr){
        head = newNode;
        head->depth = 0;
        cout<<" created  head of tree at depth 0"<<endl;
        return newNode;
    }
    while(temp){
        int compIndex = depth % k;
        cout<<" comparing index is "<<compIndex<<endl;
        if(temp->val[compIndex] <= val[compIndex]){
            cout<<" going right at depth "<<depth<<endl;
            if(temp->right) temp = temp->right;
            else{
                temp->right = newNode;
                newNode->depth = depth +1;
                return newNode;

            }
        }
        else{
            cout<<" going left at depth "<<depth<<endl;
            if(temp->left) temp = temp->left;
            else{
                temp->left = newNode;
                newNode->depth = depth + 1;
                return newNode;
            }
        }
        depth++;
    }
    return 0;

}
int main(){
    TreeNode *head= nullptr;
    int option= 1,k, maxdepth = 0;

    cout<<"enter the number of dimentsions "<<endl;
    cin>>k;
    //1 to enter new node,
    //2 to view tree
    //3 to get the depth  
    //4 to exit
    while(option != 4){
        cout<<"enter the option "<<endl;
        cin>> option;
        switch (option)
        {
            case 1:
                /* code */
                cout<<"calling node creation "<<endl;
                if(!head){
                    head = insertion(head,k);
                    cout<<head;
                }
                else{
                    TreeNode* newNode = insertion(head, k);
                    maxdepth = max(newNode->depth, maxdepth);
                }
                break;
            
            case 2:
                display(head);
                break;
            case 3 : 
                cout<<maxdepth<<" is the depth of the tree "<<endl;
                break;
        }
    }
    return 0;
}